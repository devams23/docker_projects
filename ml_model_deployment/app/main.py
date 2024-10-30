from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_pipeline



app = FastAPI()


class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    language: str


@app.get("/")
def home():
    return {"health_check": "OK", "model_version": 23}


@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    language = predict_pipeline(payload.text)
    #language = "english"
    return {"language": language}
    
