# To run this locally, you would need to install: 
# !pip install fastapi uvicorn

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(
    title="AQI Prediction API",
    description="API to predict Air Quality Index based on sub-pollutant values.",
    version="1.0.0"
)

# Load the saved Random Forest model
try:
    model = joblib.load('aqi_random_forest_model.joblib')
    print("Model loaded successfully for FastAPI app.")
except FileNotFoundError:
    print("Error: Model file 'aqi_random_forest_model.joblib' not found.")
    model = None

# Define the schema for incoming requests using Pydantic
class AQIPredictionRequest(BaseModel):
    co_aqi_value: float
    ozone_aqi_value: float
    no2_aqi_value: float
    pm2_5_aqi_value: float

@app.post("/predict")
def predict(data: AQIPredictionRequest):
    if model is None:
        raise HTTPException(status_code=500, detail="Prediction model is not available.")
    
    try:
        # Map input keys to match the exact column names used during model training
        features = pd.DataFrame([[
            data.co_aqi_value,
            data.ozone_aqi_value,
            data.no2_aqi_value,
            data.pm2_5_aqi_value
        ]], columns=['co aqi value', 'ozone aqi value', 'no2 aqi value', 'pm2.5 aqi value'])
        
        # Generate prediction
        prediction = model.predict(features)
        return {"predicted_aqi": float(prediction[0])}
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))