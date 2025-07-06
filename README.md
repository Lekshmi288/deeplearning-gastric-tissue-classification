# Deep Learning for Gastric Tumor Microenvironment (TME) Classification

Leverage the HMU-GC-HE-30K dataset from Lou et al. 2025 (https://www.nature.com/articles/s41597-025-04489-9)  to build deep learning models that classify histological image patches into eight tumor microenvironment (TME) tissue types. The dataset consists of 30,000+ patches annotated by expert pathologists across 8 tissue types relevant to gastric cancer progression. The goal is to explore TME composition patterns in gastric cancer, link them with clinical features, and lay the groundwork for biomarker discovery and prognosis modeling.

---

## 🧠 Objectives

- ✅ Develop a baseline binary classifier (Tumor vs Non-Tumor) for prototyping
- ⏳ Extend to multi-class classification (8 TME tissue types)
- ⏳ Use transfer learning (e.g., ResNet, EfficientNet)
- ⏳ Apply Grad-CAM for interpretability
- ⏳ Explore patch-level TME composition analysis per patient
- ⏳ Build basic multimodal links with clinical metadata
- ⏳ (Optional) Deploy a minimal Streamlit demo app

---

## 📊 Dataset

**Source**: [HMU-GC-HE-30K Dataset (Kaggle)]  
**Format**: 224×224 image tiles  
**Classes** (all tumor microenvironment components):

- `TUM` – Tumor epithelium  
- `STR` – Cancer-associated stroma  
- `LYM` – Lymphocyte aggregates  
- `NOR` – Normal gastric mucosa (within tumor context, for reference)  
- `ADI` – Adipose tissue  
- `MUC` – Mucus  
- `MUS` – Smooth muscle  
- `DEB` – Debris  

> ⚠️ Note: This is not a normal-vs-cancer dataset. All patches come from gastric cancer samples. Labels represent **TME composition**, not pathology status.


---

## 📂 Project Structure

deeplearning-gastric-tissue-classification/
├── Data/ # Raw image patches (not uploaded)
├── notebooks/ # EDA, training notebooks
├── src/ # Python scripts (training, models, utils)
├── outputs/ # Saved models, logs, metrics
├── README.md


---

## 🛠️ Progress Tracker

- [x] Environment setup
- [x] Dataset exploration
- [ ] Binary classification pipeline (Tumor vs Non-Tumor)
- [ ] Multi-class classifier for all 8 tissue types
- [ ] Grad-CAM visualizations for model explanation
- [ ] Compute TME composition (% per tissue per patient)
- [ ] Merge image-level features with clinical metadata
- [ ] Statistical modeling or ML-based prognosis predictions
- [ ] Streamlit deployment (optional)

## 📌 Notes

- Some tissue classes (e.g., adipose, smooth muscle) are biologically “normal” tissues but still part of the **tumor context** and can play roles in progression or immune evasion.
- All image patches are annotated by a 3-step expert pipeline and extracted from .svs whole-slide images.

---

**License**: Follows terms provided by the original dataset (open for research use).



# Deep Learning for Gastric Tissue Classification in Histopathology Images

This project explores deep learning approaches to classify H&E-stained gastric histopathology image tiles into biologically meaningful tissue types. The dataset includes over 30,000 annotated patches across 8 categories, including tumor, normal, and tumor-associated tissue classes.

The project starts with a **baseline binary classification task** (Tumor vs Non-Tumor) to validate the pipeline and model performance. The goal is to extend it to **multi-class tissue classification**, followed by **model explainability using Grad-CAM** and potential deployment via a simple Streamlit interface.

---

## 🧠 Objectives
- ✅ Build a baseline binary classifier (Tumor vs Non-Tumor)
- ⏳ Extend to multi-class classification (8 tissue types)
- ⏳ Use transfer learning (e.g., ResNet, EfficientNet)
- ⏳ Apply Grad-CAM for model interpretability
- ⏳ Deploy a lightweight Streamlit app for demo

---

## 📊 Dataset
- Source: [Gastric Cancer Histopathology Dataset – Kaggle](https://www.kaggle.com/datasets/orvile/gastric-cancer-histopathology-tissue-image-dataset)
- 31,096 image tiles (224×224 px)
- 8 tissue types:
  - TUM (Tumor), STR (Stroma), NORM (Normal), LYM, MUC, ADI, MUS, DEB

---

## 📂 Project Structure

deeplearning-gastric-tissue-classification/
├── data/ # Raw images (external, not uploaded)
├── notebooks/ # Jupyter notebooks for EDA, training
├── src/ # Python modules and training scripts
├── outputs/ # Saved models, logs, results
├── README.md


---

## 📌 Progress Tracker
- [x] Environment setup
- [ ] Dataset exploration
- [ ] Binary classification pipeline (Tumor vs Non-Tumor)
- [ ] Multi-class model
- [ ] Grad-CAM visualizations
- [ ] Streamlit deployment

---
