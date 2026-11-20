
from fastapi import FastAPI
from pydantic import BaseModel, Field
import pandas as pd
import joblib
from pathlib import Path

app = FastAPI(title="NYC Airbnb Price Prediction API")

# Load the trained ML pipeline
MODEL_PATH = Path(__file__).with_name("airbnb_price_pipeline.pkl")
model = joblib.load(MODEL_PATH)


# Input features required by the model
class ListingFeatures(BaseModel):
    neighbourhood_cleansed: str
    room_type: str
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    accommodates: int = Field(ge=1)
    bedrooms: float = Field(ge=0)
    bathrooms_numeric: float = Field(ge=0)


# Home route
@app.get("/")
def home():
    return {
        "message": "NYC Airbnb Price Prediction API is running!"
    }


# Prediction route
@app.post("/predict")
def predict_price(listing: ListingFeatures):

    input_df = pd.DataFrame([listing.model_dump()])

    prediction = model.predict(input_df)[0]

    return {
        "predicted_price_usd": round(float(prediction), 2),
        "currency": "USD"
    }
