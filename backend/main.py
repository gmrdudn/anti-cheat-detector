import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

app = FastAPI(title="Valorant Anti Cheat Detector")
model = joblib.load("cheat_model.pkl")
class Telemetry(BaseModel):
    reaction_ms: float
    delta_x: float
    delta_y: float
    click_intervals: list[float]
    recoil_errors: list[float]

@app.get("/")
def home():
    return {"status": "server running"}

@app.post("/detect")
def detect(data: Telemetry):
    score = 0

    if data.reaction_ms < 120:
        score += 20

    if abs(data.delta_x) > 300 and abs(data.delta_y) > 300:
        score += 25

    if len(data.click_intervals) > 3:
        if np.std(data.click_intervals) < 5:
            score += 20

    if len(data.recoil_errors) > 3:
        if np.std(data.recoil_errors) < 1.5:
            score += 25

    final_score = min(score, 100)

    return {
        "risk_score": final_score,
        "verdict": "suspicious" if final_score >= 50 else "normal"
    }

import pandas as pd

@app.get("/report")
def report():
    df = pd.read_csv("sample_data.csv")

    total_players = len(df)
    cheat_players = len(df[df["label"] == "cheat"])
    avg_reaction = round(df["reaction_ms"].mean(), 2)
    cheat_ratio = round((cheat_players / total_players) * 100, 2)

    return {
        "total_players": total_players,
        "cheat_players": cheat_players,
        "average_reaction_ms": avg_reaction,
        "cheat_ratio_percent": cheat_ratio
    }

@app.post("/predict")
def predict(data: Telemetry):
    input_data = [[
        data.reaction_ms,
        data.delta_x,
        data.delta_y,
        float(np.std(data.click_intervals)),
        float(np.std(data.recoil_errors))
    ]]

    prediction = model.predict(input_data)[0]

    return {
        "prediction": prediction,
        "message": "핵 의심" if prediction == "cheat" else "정상 유저"
    }