# 📊 Telecom Churn Prediction – End-to-End ML Engineering System (V2)

## 🧠 Project Overview

This project implements a complete **Machine Learning Engineering system for telecom customer churn prediction**, designed with a strong focus on modularity, reproducibility, and production readiness.

Instead of focusing only on model training, the system is engineered as a full end-to-end ML pipeline that separates:

- Data processing  
- Feature engineering  
- Model training  
- Experiment tracking  
- Model evaluation  
- Deployment  

The system compares multiple machine learning models (**Random Forest, XGBoost, LightGBM**) using **GridSearchCV and cross-validation**, and selects the best-performing model based on **ROC-AUC and classification metrics**.

The final model is deployed as a production-ready service using **FastAPI** and **Docker**, with full experiment tracking using **MLflow** and version control via **Git + GitHub**.

---

## 🏗️ Architecture

```
Raw Data
   ↓
EDA & Feature Engineering
   ↓
Training Pipeline
   ├── Random Forest
   ├── XGBoost
   └── LightGBM
          ↓
GridSearchCV + Cross-Validation
          ↓
MLflow Tracking & Experiment Logging
          ↓
Best Model Selection (ROC-AUC)
          ↓
Production Inference Pipeline
          ↓
FastAPI REST API
          ↓
Dockerized Deployment
```
---

## 🚀 Tech Stack

### Core Tools
- Python 3.10+
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- LightGBM
- Random Forest

### MLOps & Engineering
- MLflow (experiment tracking)
- Git + GitHub (version control)
- FastAPI (REST API)
- Docker (containerization)

### Visualization & Evaluation
- Matplotlib
- Seaborn
- ROC Curve analysis
- AUC score
- Confusion matrix

---

## 📊 Machine Learning Pipeline

1. Environment setup (Conda + dependencies)
2. Project structure creation (modular architecture)
3. Data loading module
4. Exploratory Data Analysis (EDA)
5. Feature engineering pipeline
6. Model training:
   - Random Forest
   - XGBoost
   - LightGBM
7. Hyperparameter tuning (GridSearchCV + cross-validation)
8. MLflow experiment tracking (in code modules only)
9. Model comparison using ROC-AUC
10. Best model selection
11. FastAPI deployment
12. Docker containerization

---

## 🚀 Tech Stack

### Core Tools
- Python 3.10+
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- LightGBM
- Random Forest

### MLOps & Engineering
- MLflow (experiment tracking)
- Git + GitHub (version control)
- FastAPI (REST API)
- Docker (containerization)

### Visualization & Evaluation
- Matplotlib
- Seaborn
- ROC Curve analysis
- AUC score
- Confusion matrix

---

## 📊 Machine Learning Pipeline

1. Environment setup (Conda + dependencies)
2. Project structure creation (modular architecture)
3. Data loading module
4. Exploratory Data Analysis (EDA)
5. Feature engineering pipeline
6. Model training:
   - Random Forest
   - XGBoost
   - LightGBM
7. Hyperparameter tuning (GridSearchCV + cross-validation)
8. MLflow experiment tracking (in code modules only)
9. Model comparison using ROC-AUC
10. Best model selection
11. FastAPI deployment
12. Docker containerization

---

## 📁 Project Structure
```
telecom_churn_v2/
│
├── src/
│ ├── data/
│ ├── features/
│ ├── training/
│ ├── evaluation/
│ ├── inference/
│ └── utils/
│
├── notebooks/
│ └── EDA_analysis.ipynb
│
├── api/
│ └── main.py
│
├── models/
├── mlruns/
├── Dockerfile
├── requirements.txt
└── README.md
```


---

## 📈 Model Evaluation

Models are evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC (**primary metric**)

### Visualizations:
- ROC curve comparison (all models)
- AUC comparison
- Confusion matrix

---

## 🧠 MLflow Tracking

MLflow is used inside training modules to track:

- Hyperparameters (GridSearchCV results)
- Metrics (accuracy, precision, recall, F1, ROC-AUC)
- Model artifacts
- Best model selection

---

## 🚀 FastAPI Deployment

Run API locally:

```uvicorn api.main:app --reload
Access:

http://127.0.0.1:8000/docs
```
## 🐳 Docker Deployment

### Build image

```
docker build -t telecom-churn-api .
```
Run container
```
docker run -p 8000:8000 telecom-churn-api
```
## 🔁 Git & GitHub Workflow

This project follows continuous version control:

- Git used from day one
- Commits after each stable milestone:
  - setup
  - EDA
  - training pipeline
  - MLflow integration
  - API development
  - Dockerization

Final version is pushed to GitHub as a stable production-ready release.

---

## 📌 Key Engineering Highlights

- End-to-end ML system design
- Modular Python architecture
- Multi-model comparison (RF, XGBoost, LightGBM)
- GridSearchCV hyperparameter tuning
- MLflow experiment tracking (production style)
- ROC-AUC based model selection
- FastAPI deployment
- Docker containerization
- GitHub version-controlled workflow

---

## 🎯 Learning Outcomes

- ML system design (end-to-end pipeline)
- MLOps fundamentals (MLflow + Git + Docker)
- Model evaluation using ROC-AUC
- Production API development with FastAPI
- Containerized ML deployment
- Reproducible ML engineering workflows

---

### Focus Areas

- Machine Learning Systems
- MLOps & Deployment
- LLM & NLP Engineering
- Cloud AI (Azure / AWS roadmap)

## 👤 Author

**Alvaro Vega**  
Aspiring AI Engineer | Machine Learning Engineer | ML & LLM Systems

### 🧠 Project Context

This repository is part of a structured learning path focused on building **production-grade Machine Learning Engineering systems**, including modular ML architecture, MLOps practices, and cloud deployment readiness.

### 🔗 GitHub

https://github.com/Javier-DataScience


