# 📊 Telecom Churn Prediction – End-to-End ML System

## 🧠 Project Overview
This project is an end-to-end machine learning system to predict customer churn using historical telecom data. It includes data preprocessing, feature engineering, model training, hyperparameter tuning, threshold optimization, experiment tracking with MLflow, and deployment using FastAPI and Docker.

---

## 🚀 Tech Stack
- Python
- XGBoost
- Scikit-learn
- Pandas / NumPy
- MLflow (experiment tracking)
- FastAPI (model serving API)
- Docker (containerization)
- Joblib (model serialization)

---

## 📊 ML Pipeline

1. Data preprocessing
2. Exploratory Data Analysis (EDA)
3. Feature engineering
4. Model training (XGBoost)
5. Hyperparameter tuning
6. Threshold optimization
7. MLflow experiment tracking
8. Final model selection
9. Model serialization
10. FastAPI deployment
11. Docker containerization

---

## 📦 Project Structure
telecom_churn_project/
│
├── notebooks/ # EDA + MLflow experiments
├── src/
│ └── app.py # FastAPI app
├── models/
│ └── xgboost_model.pkl # Trained model
├── requirements.txt
├── Dockerfile
└── README.md

---

## 🚀 How to Run the Project

### 1. Clone repository
```bash
git clone https://github.com/Javier-DataScience/telecom-churn-ml-api.git
cd telecom-churn-ml-api
2. Run with Docker
docker build -t telecom-churn-api .
docker run -p 8000:8000 telecom-churn-api
3. Access API
http://127.0.0.1:8000/docs
________________________________________
📈 Model Performance
•	Model: XGBoost 
•	Optimization: GridSearchCV + Threshold tuning 
•	Tracking: MLflow 
________________________________________
📌 Key Learning Outcomes
•	End-to-end ML pipeline design 
•	Model deployment with FastAPI 
•	Containerization with Docker 
•	Experiment tracking with MLflow 
________________________________________
👨‍💻 Author
Javier Data Science Project

---

# 🚀 STEP 2 — Commit README

After saving:

```bash
git add README.md
git commit -m "Add professional README for portfolio"
git push

