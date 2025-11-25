# -*- coding: utf-8 -*-

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("./pipeline.joblib")

class Input(BaseModel):
    CUST_NBR: str
    MENU_TYP_DESC: str
    PYR_SEG_CD: str
    DIV_NBR: str
    WKLY_ORDERS: float
    PERC_EB: float
    AVG_WKLY_SALES: float
    AVG_WKLY_CASES: float

class Output(BaseModel):
    prediction: list[int]

@app.post("/predict", response_model=Output)
def predict(data: list[Input]) -> Output:
    print(data)
    data = [item.model_dump() for item in data]
    data = pd.DataFrame(data)
    prediction = model.predict(data).tolist()
    return {"prediction":prediction}

@app.get("/")
def home():
    return RedirectResponse(url="/docs", status_code=302)