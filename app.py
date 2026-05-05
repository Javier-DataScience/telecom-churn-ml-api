from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import joblib
import numpy as np

app = FastAPI()

# Load model at startup
config = joblib.load("models/xgboost_model.pkl")

model = config["model"]
imputer = config["imputer"]
threshold = config["threshold"]


# Input schema
class InputData(BaseModel):
    data: List[float]


@app.get("/")
def home():
    return {"message": "Churn prediction API is running"}


@app.post("/predict")
def predict(input_data: InputData):

    # Convert input to numpy array
    X = np.array(input_data.data).reshape(1, -1)

    # Apply preprocessing
    X_clean = imputer.transform(X)

    # Predict probability
    proba = model.predict_proba(X_clean)[0][1]

    # Apply threshold
    prediction = int(proba >= threshold)

    return {
        "prediction": prediction,
        "probability": float(proba)
    }