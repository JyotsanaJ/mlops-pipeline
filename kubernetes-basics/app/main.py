from fastapi import FastAPI
from pydantic import BaseModel, Field
from helper import Naive_Bayes
from typing import List
import numpy as np


app = FastAPI()
model = Naive_Bayes()

class Request(BaseModel):
    data : List = []

@app.get("/")
def read_root():
    return {"About": "Khoros actiongen API"}

@app.post("/predict")
def predict_species(request: Request):
    data = np.array(request.data)
    data = data.reshape(-1,4)
    response = model.prediction(data)
    return {"Species": response}