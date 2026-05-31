from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("model.pkl")

class House(BaseModel):
    area: int

@app.get("/")
def health():
    return {"status": "healthy"}

@app.post("/predict")
def predict(data: House):

    prediction = model.predict([[data.area]])[0]

    return {
        "area": data.area,
        "predicted_price": round(prediction)
    }
