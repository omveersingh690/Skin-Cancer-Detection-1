# 🩺 Skin Cancer Detection Application

A machine learning-powered application for early and accurate detection of skin cancer using image classification techniques.

## 📸 Overview

This application uses deep learning to analyze images of skin lesions and classify them as benign or malignant. The goal is to assist in early detection and raise awareness about skin health.

## 🚀 Features

- 🔍 Upload or capture an image of a skin lesion
- 🧠 Uses trained deep learning models for classification
- 📊 Displays prediction results with confidence score
- 💬 Provides health recommendations and encourages medical consultation
- 🌐 User-friendly interface (Web/Mobile)

## 🧰 Tech Stack

- **Frontend**: HTML, CSS, JavaScript / React Native / Flutter (Choose yours)
- **Backend**: Python (Flask / Django)
- **Machine Learning**: TensorFlow / PyTorch, CNN Model
- **Deployment**: Render / Heroku / Vercel / Firebase
- **Database**: SQLite / Firebase / MongoDB (if applicable)

## 🧪 Model Training

- Dataset used: [ISIC Skin Cancer Dataset](https://www.isic-archive.com/)
- Preprocessing: Image resizing, augmentation, normalization
- Architecture: CNN (Convolutional Neural Network)
- Accuracy: ~XX% (adjust with your results)

## 🛠️ Installation & Run Locally

```bash
# Clone the repository
git clone https://github.com/your-username/skin-cancer-detection.git
cd skin-cancer-detection

# Backend setup
cd backend
pip install -r requirements.txt
python app.py

# Frontend setup (if separate)
cd frontend
npm install
npm start




for review 2


# Skin Cancer Detection - Data Visualization

## 🎯 Objective
To visualize and communicate the insights derived from the skin cancer detection model using charts, metrics, and interactive features.

## 📁 Dataset
- Source: [HAM10000 Dataset](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000)
- Number of classes: 7
- Binary labels used: Benign / Malignant

## 📊 Visualizations Included
1. Class Distribution (Pie Chart)
2. Image Count per Class (Bar Chart)
3. Model Evaluation Metrics (Grouped Bar Chart)
4. Confusion Matrix (Heatmap)
5. ROC Curve (Line Plot)
6. Feature Importance (if applicable)

## 🛠 Tools Used
- Power BI / Python (Plotly, Seaborn, Matplotlib)
- Jupyter Notebook / Streamlit App

## ⚡ Interactivity Features
- Tooltip Hover
- Zoom on ROC
- Filtering by model version

## 📜 Interpretation
- The model achieves 87% accuracy.
- Highest misclassification between melanoma and benign.
- ROC AUC: 0.91 indicating strong performance.

## 📎 Instructions to Run
1. Clone the repo.
2. Open the Power BI file / Run the Streamlit app.
3. Explore using provided filters and tooltips.

