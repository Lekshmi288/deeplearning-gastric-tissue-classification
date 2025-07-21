# Deep Learning for Gastric Tumor Microenvironment (TME) Classification

Leverage the [HMU-GC-HE-30K dataset](https://www.nature.com/articles/s41597-025-04489-9) from Lou et al. (2025) to build deep learning models that classify histological image patches into eight tumor microenvironment (TME) tissue types.

TME components play a critical role in gastric cancer progression, immune tolerance, and treatment response. However, detailed TME-annotated image datasets are scarce. This dataset addresses that gap by providing 30,000+ expert-labeled patches across eight biologically meaningful tissue types, along with matched clinical metadata.

Unlike simple tumor vs non-tumor classification, which provides only coarse segmentation, TME-based classification captures the diverse cellular and structural components within the tumor region that are known to influence tumor progression, immune evasion, and treatment response. By modeling these fine-grained patterns, this project focuses on:

- Building and evaluating deep learning models for patch-level TME classification
- Using Grad-CAM and prediction confidence to interpret model decisions
- Identifying common failure cases and potential data issues through visualization
- Building an interactive Streamlit app to audit model predictions and visualize Grad-CAM heatmaps, helping bridge the gap between AI-based histology models and expert review in high-stakes domains like cancer diagnosis.

---

## Project Deliverables
 ✔️ Multi-class classifier (EfficientNetB3) for 8 TME tissue classes
 
 ✔️ Grad-CAM for model interpretability and debugging
 
 ✔️ Patch-level prediction audit and confidence analysis
 
 ✔️ Analysis notebooks covering training, misclassifications, and error cases
 
 ✔️ Interactive Streamlit demo: PathoPredictX-GC


---

## Dataset

**Source**: HMU-GC-HE-30K Dataset
**Format**: 224×224 image tiles  
**Classes** (all tumor microenvironment components):

- `ADI` – Adipose
- `DEB` – Debris
- `LYM` – Lymphocytes
- `MUC` – Mucus
- `MUS` – Smooth Muscle  
- `STR` – Cancer-associated Stroma  
- `NOR` – Normal Gastric Mucosa (NORM)
- `TUM` – Tumor


---

## Model Architecture and Training

- Pretrained EfficientNetB3 fine-tuned for 8-way classification
- Early stopping and learning rate scheduling
- Model evaluation using macro F1 and confusion matrix

---

## [PathoPredictX-GC](https://huggingface.co/spaces/Lekshmi288/PathoPredictX-GC) : Interactive Auditing & Interpretability Tool

As part of this project, I built PathoPredictX-GC, a lightweight Streamlit app that enables visual auditing of model predictions in gastric cancer histopathology.

Key Features:

   - Predicts tissue type from any 224×224 histology patch

   - Visualizes class-specific attention using Grad-CAM

   - Displays prediction confidence alongside ground truth

   - Helps spot:

       - Model confusion in mixed-tissue regions

       - Label noise or annotation errors

       - Poor staining or image artifacts


Why it matters:

This tool supports interpretability, quality control, and human-AI collaboration:

   - When predictions diverge from the ground truth, Grad-CAM helps assess whether the model made a biologically reasonable call, which is useful for identifying label issues.

   - In the absence of ground truth, confidence scores and attention maps provide a second-opinion system for expert review.

   - Helps researchers identify blind spots in model performance and surface underlying data issues.

Use it here: https://huggingface.co/spaces/Lekshmi288/PathoPredictX-GC

---

## Repository Structure

```
deeplearning-gastric-tissue-classification/
│
├── notebooks/               # EDA, training notebooks
├── validation_results/      # CSV files showing the validation results 
├── PathoPredictX-GC-app/    # Streamlit app files
│   ├── src/
│   ├── Dockerfile
│   └── requirements.txt
└── README.md
```


---


## 📌 Notes

- Some tissue classes (e.g., adipose, smooth muscle) are biologically “normal” tissues but still part of the **tumor context** and can play roles in progression or immune evasion.
- This is not a normal vs cancer dataset. All patches come from gastric cancer samples.
- No clinical prediction modeling was attempted due to a lack of sufficient metadata integration. While the clinical metadata of the patients was provided as a CSV file, no mapping between the image files and the metadata was available. 
