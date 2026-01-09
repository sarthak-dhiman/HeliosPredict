import os, joblib
import pandas as pd
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel

from tensorflow import keras

# Paths
RF_MODEL = Path("models/rf_model.joblib")
NN_MODEL = Path("models/nm_model.h5")
PREPROC = Path("models/preprocessor.joblib")

# Load preprocessor
preproc = joblib.load(PREPROC)

# Load model
if NN_MODEL.exists():
    model = keras.models.load_model(NN_MODEL, compile=False)
    model_type = "nn"
elif RF_MODEL.exists():
    model = joblib.load(RF_MODEL)
    model_type = "rf"
else:
    raise RuntimeError("No model file found in /models")

# Input schema
class WeatherIn(BaseModel):
    uv_index: float
    condition: str
    cloud_cover: float
    temp_c: float
    humidity: float
    wind_kph: float
    hour: int | None = None
    month: int | None = None
    day_of_year: int | None = None

app = FastAPI(title="HeliosPredict")

@app.get("/health")
def health():
    return {"ok": True, "model": model_type}

@app.post("/predict")
def predict(x: WeatherIn):
    X = pd.DataFrame([x.model_dump()])
    Xp = preproc.transform(X)

    if model_type == "nn":
        y = float(model.predict(Xp, verbose=0)[0][0])
    else:
        y = float(model.predict(Xp)[0])

    return {"predicted_power_kw": round(y, 3)}
