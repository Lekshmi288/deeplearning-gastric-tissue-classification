
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
