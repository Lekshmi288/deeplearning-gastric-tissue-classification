#!/usr/bin/env python
# coding: utf-8

# In[5]:

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import time
import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
from gradcam_visualization import histo_GradCAM
import random



@st.cache_resource
def load_model():
    return tf.keras.models.load_model("src/efficientnetb3_baseline.h5")
 

best_model= load_model()

# if best_model is None:
#     st.stop() 

# try:
#     dummy= np.zeros((1, 224, 224, 3), dtype=np.float32)
#     preds= best_model.predict(dummy)
#     st.success("Dummy prediction succeeded. Model is usable.")
#     st.write("Dummy prediction output:", preds)
# except Exception as e:
#     st.error(f"Model is not usable: {e}")
#     st.stop()





st.set_page_config(page_title="PathoPredictX-GC", layout="wide")
# st.title("PathoPredictX-GC")

# st.markdown("* A deep learning-based application for interpreting and auditing tissue classification in Gastric cancer histopathology.*")
st.markdown(
    """
    <div style='text-align: center;'>
        <h1>PathoPredictX-GC</h1>
        <p style='font-style: italic; color: #ccc; font-size: 1.25em; margin-bottom: 36px;'>
            A deep learning-based application for interpreting and auditing tissue classification in Gastric cancer histopathology.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

info_col, app_col= st.columns([1, 1.5])

with info_col:
    st.markdown("""
    **PathoPredictX-GC** is an interactive audit and interpretability tool for AI-based tissue classification in gastric cancer histopathology.  \n
    It enables researchers and pathologists to:
 
    - **Predict tissue type:** Classifies one of 8 tumor microenvironment (TME) tissue types from H&E-stained gastric cancer slide images.
    - **Audit predictions:** Visualize which image regions most influenced each classification using Grad-CAM, helping verify that model decisions align with known histological features.
    - **Check prediction confidence:** Quickly identify ambiguous or borderline cases for closer review.
    - **Support quality control:** Spot potential model failures, misclassifications, or even mislabeled data thereby improving trust and reducing errors in AI-driven studies.

    **Use cases:**

    - When model and ground truth disagree, the tool helps determine if the model’s decision makes sense based on the highlighted regions. This is useful for catching annotation errors or discovering unexpected tissue features.
    - When no ground truth is available, the visual and confidence feedback provides a “second opinion” for expert review and documentation.
    
    **Tissue types classified:**
    
     Adipose (ADI), Debris (DEB), Lymphocytes (LYM), Mucus (MUC), Smooth Muscle (MUS), Normal Colon Mucosa (NORM), Cancer-associated Stroma (STR), Tumor (TUM)  
    
    This tool helps bridge the gap between AI-based histology models and expert review, especially in high-stakes domains like cancer diagnosis.
    """)
    
    with st.expander("About the model"):
        st.markdown("""
    - **Architecture:** EfficientNetB3 + Softmax  
    - **Trained on:** 31,096 H&E-stained 224×224 tissue images from gastric cancer slides at Harbin Medical University Cancer Hospital. See: https://doi.org/10.6084/m9.figshare.25954813
    - **Classes:** ADI, DEB, LYM, MUC, MUS, NOR, STR, TUM  
    - **Use case:** Supports model auditing and interpretability 
    """)
    
        
    with st.expander("Disclaimer"):
        st.warning("This tool is intended for research and demonstration only. Not for clinical use.")


with app_col:

    if "file_uploader_key" not in st.session_state:
        st.session_state["file_uploader_key"]= 0

    if "sample_select_key" not in st.session_state:
        st.session_state["sample_select_key"]= 0

    sample_dir = "src/sample_images"
    if "shuffled_sample_images" not in st.session_state or st.session_state.get("shuffle_reset", False):
        sample_images= [img for img in os.listdir(sample_dir) if img.lower().endswith('.png')]
        random.shuffle(sample_images)
        st.session_state["shuffled_sample_images"]= sample_images
        st.session_state["shuffle_reset"]= False
    else:
        sample_images = st.session_state["shuffled_sample_images"]

    st.info("📤 Upload your own tissue image patch or select a sample image below for testing.")
    
    uploaded_file= st.file_uploader("Upload a tissue image patch", type=["jpg", "png", "jpeg"], key=f"file_uploader_{st.session_state['file_uploader_key']}")
    
    selected_sample= st.selectbox("Or choose a sample image:",["-- Select a sample --"] + sample_images,index=0, key=f"sample_select_{st.session_state['sample_select_key']}")

    if st.button("Reset"):
        st.session_state["file_uploader_key"] += 1
        st.session_state["sample_select_key"] += 1
        st.session_state["shuffle_reset"] = True
        st.rerun()

    tissue_image = None

    
    if selected_sample!= "-- Select a sample --":
        tissue_image_path= os.path.join(sample_dir, selected_sample)
        tissue_image= image.load_img(tissue_image_path)
        st.success(f"📁 Using Image: {selected_sample}")
        
    elif uploaded_file is not None:
        st.success("📁 File uploaded successfully!")
        st.write("Uploaded: ", uploaded_file.name)
        tissue_image = image.load_img(uploaded_file)
    


    if tissue_image is not None:
        tissue_types= ['ADI', 'DEB', 'LYM', 'MUC', 'MUS', 'NOR', 'STR', 'TUM']
        st.markdown("🔬 Select the true tissue type below.  \n"
            "*For sample images, the true class is given before the underscore in the file name (e.g., 'MUC_45.png' means true class is MUC).*  \n"
            "*For the uploaded images, if you do not know the ground truth, choose 'Unknown'.*")

        
        options= ["-- Select tissue type --", "Unknown"] + tissue_types
        true_class= st.selectbox("Select the true tissue type:",options=options,index=0)
    
        
        if true_class!= "-- Select tissue type --":
            if true_class== "Unknown":
                true_class= None
        
            try:
                #tissue_image= image.load_img(uploaded_file)
                #st.info("Image loaded successfully.")
        
                tissue_image_array= image.img_to_array(tissue_image)
                #st.info(f"Image converted to array. Shape: {tissue_image_array.shape}")
        
                result= histo_GradCAM(best_model,tissue_image_array,true_class)
                st.success("Analysis done! 💯 Ready to peek inside the black box? 🔍")
                
                # if true_class is not None:
                #     st.markdown(f"**True Class:** {true_class}")
                # st.markdown(f"**Predicted Class:** {result['pred_class']}")
                # st.markdown(f"**Prediction Confidence:** {result['pred_prob']:.2f}")

                if true_class is not None:
                    match= (true_class==result['pred_class'])
                    emoji= "✅" if match else "⚠️"
                    st.markdown(f"{emoji} **True Class:** {true_class}")
                    
                st.markdown(f"🏷️ **Predicted Class:** {result['pred_class']}")
                st.markdown(f"📈 **Prediction Confidence:** {result['pred_prob']:.4f}")

                low_conf_threshold= 0.6
                high_conf_threshold= 0.9
                is_low_conf= result['pred_prob']<low_conf_threshold
                is_high_conf= result['pred_prob']>high_conf_threshold
                
                if true_class is not None:
                    if is_low_conf and match:
                        st.warning("⚠️ Low-confidence prediction. Compare the highlighted regions with your expert knowledge to assess if the model’s focus makes sense for this tissue type.")

                    if is_low_conf and not match:
                        st.warning("⚠️ Low-confidence prediction. The model is uncertain and disagrees with the true class. Review the highlighted regions and apply your expert judgment.")
                    
                    elif is_high_conf and not match:
                        st.warning("⚠️ High-confidence prediction does not match the ground truth."
                                      "Inspect the highlighted regions. This could be a model error or a mislabeled ground truth.")

                    elif not match:
                        st.warning("⚠️ Prediction does not match the ground truth. Inspect the highlighted regions and see if the regions the model focused on match what you would expect for this tissue type.")

                else:
                    if is_low_conf:
                         st.warning("⚠️ Low-confidence prediction. Since ground truth is unknown, have a pathologist review this sample before making any decisions."
                                    "Inspect the highlighted regions to see if the model focused on meaningful tissue regions.")

                        
                col1, col2 = st.columns(2)
                # col1.image(result['original'], caption="Tissue Image Patch", use_container_width=True)
                # col2.image(result['overlay'], caption="Regions influencing prediction", use_container_width=True)
                #col1.subheader("Uploaded Tissue Image Patch")
                col1.markdown("<h4 style='text-align: center;'>Uploaded Tissue Image Patch</h4>", unsafe_allow_html=True)
                col1.image(result['original'], width=540)
                col2.markdown("<h4 style='text-align: center;'>Regions influencing prediction</h4>", unsafe_allow_html=True)
                #col2.subheader("Regions Influencing Prediction")
                col2.image(result['overlay'],width=540)

                st.info("💡 In the image on the right, red and yellow areas show where the model focused most for its prediction.")

       
            except Exception as e:
                st.error(f"Error during prediction or visualization: {e}")
                





# In[ ]:




