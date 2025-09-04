import os, joblib
from pathlib import Path
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

TF_MODEL = Path("models/best_model_nn.keras")
PREPROC = Path("models/preprocessor.joblib")
SK_MODEL = Path("models/best_model.joblib")

preproc = joblib.load(PREPROC)

if TF_MODEL.exists():
    from tensorflow import keras
    model = keras.models.load_model(TF_MODEL, compile=False)
    model_type = "nn"
else:
    import joblib as jl
    model = jl.load(SK_MODEL)
    model_type = "sklearn"

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
