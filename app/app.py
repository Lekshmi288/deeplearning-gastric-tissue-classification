#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
from utils.gradcam_visualization import histo_GradCAM

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("model/efficientnetb3_baseline.h5")

best_model = load_model()

st.title("PathoPredictX-GC")

st.markdown("""
*A deep learning tool for prediction, interpretability, and decision support in Tumor Microenvironment (TME) profiling of gastric cancer histopathology.*

**PathoPredictX-GC** predicts and explains histological classifications across **8 TME tissue types** — including tumor, normal mucosa, stroma, lymphocytes, and more.  
It is designed to support **pathologists and cancer researchers** in:

- **Auditing model decisions** using Grad-CAM visualizations  
- **Understanding prediction confidence** and probable misclassifications  
- **Interpreting model performance** across subtle and ambiguous tissue boundaries  

**Tissue types classified:**

- Adipose (ADI)  
- Debris (DEB)  
- Lymphocytes (LYM)  
- Mucus (MUC)  
- Smooth Muscle (MUS)  
- Normal Colon Mucosa (NORM)  
- Cancer-associated Stroma (STR)  
- Tumor (TUM)  

This tool helps bridge the gap between AI-based histology models and expert review in gastric cancer diagnostics.
""")

with st.expander("About the model"):
    st.markdown("""
- **Architecture:** EfficientNetB3 + Softmax  
- **Trained on:** 31,096 H&E-stained 224×224 tissue images from gastric cancer slides at Harbin Medical University Cancer Hospital, extracted using tissue heatmaps annotated from a public colorectal cancer dataset.  
  *(HMU-GC-HE-30K dataset, see: https://doi.org/10.6084/m9.figshare.25954813)*
- **Classes:** ADI, DEB, LYM, MUC, MUS, NOR, STR, TUM  
- **Use case:** Supports model auditing and interpretability  
    """)

    
with st.expander("Disclaimer"):
    st.warning("This tool is intended for research and demonstration only. Not for clinical use.")

    
uploaded_file = st.file_uploader("Upload a tissue image patch", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    tissue_image = image.load_img(uploaded_file)
    tissue_image_array= image.img_to_array(tissue_image)
    result = histo_GradCAM(best_model,tissue_image_array)

    st.markdown(f"**Predicted Class:** {result['pred_class']}")
    st.markdown(f"**Prediction Confidence:** {result['pred_prob']:.2f}")

    col1, col2 = st.columns(2)
    col1.image(result['original'], caption="Original Histology Image", use_column_width=True)
    col2.image(result['overlay'], caption="Grad-CAM Overlay (Model Attention)", use_column_width=True)



# In[ ]:




