from fastapi.dependencies import models
from pydantic import BaseModel

import os
import joblib
from fastapi import FastAPI

app = FastAPI()

# Get the directory where main1.py is currently located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build the absolute path to the model file
model_path = os.path.join(BASE_DIR, "firstmodel.pkl")

app = FastAPI()

class datascience(BaseModel):
    studyHours: float


# api end point

@app.get("/")
def test():
    return {"message": "uvicorn is running"}

@app.post("/predict")
def datainsert(ds:datascience):
    marks = models.predict([[ds.studyHours]])
    return{"predictionmarks":round(float(marks[0]),2)}