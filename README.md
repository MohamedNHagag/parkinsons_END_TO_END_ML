# 🧠 Parkinson's Disease Prediction - End-to-End ML Project

This is a complete End-to-End Machine Learning project that predicts whether a person has Parkinson's Disease based on biomedical voice measurements.

## 🚀 Project Overview

This project walks through the full ML lifecycle:

1. **Data Ingestion** - Load and split the dataset into training and testing sets.
2. **Data Transformation** - Clean and scale the data using a preprocessing pipeline.
3. **Model Training** - Train multiple classification models and select the best one using evaluation metrics.
4. **Model Evaluation** - Evaluate the best model using accuracy and F1-score.
5. **Model Deployment** - Use Streamlit to create a web interface for predictions.

---

## 📁 Project Structure
.
├── src/
│ ├── components/
│ │ ├── ingestion.py
│ │ ├── trainsformation.py
│ │ ├── trainer.py
│ │ ├── evaluate.py
│ │ └── utils.py
│ ├── exception.py
│ ├── logger.py
├── artifacts/ (contains trained models and preprocessors)
├── logs/ (log files)
├── app.py (Main execution script)
├── streamlit_app.py (Streamlit UI for prediction)
├── README.md


## 📊 Dataset

- Source: UCI Parkinson's Dataset
- Path: `NoteBook/Dataset/parkinsons.data`
- Target Column: `status`  
  - `1`: Parkinson’s disease  
  - `0`: Healthy

---

## ⚙️ How to Run

### 1. Install Requirements

```bash
pip install -r requirements.txt


📈 Models Used
Logistic Regression
Decision Tree
Random Forest
KNN
AdaBoost
XGBoost
CatBoost
SVM
The best model is selected based on F1-score.


📬 Contact
Author: Mohamed Nasser Abohamda
LinkedIn:www.linkedin.com/in/mohamed-hagag-a117682a7
GitHub:https://github.com/MohamedNHagag
Email: hagag9868@gmail.com

