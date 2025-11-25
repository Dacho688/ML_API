---
title: ML API
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
pinned: false
---
## ML API
A FastAPI enpoint serving a fitted sklearn pipeline with an ordinal logistic regression model using the 
<a href="https://pypi.org/project/mord/">Mord Python Package</a> to predict customer's "small quantity order importance ranking (1-10)." 

#### Pipeline Steps
1. Column Transformer<br>
        a. Standard Scaling for numerical variables<br>
        b. One-hot-encoding for categorical variables
2. Feature Selection<br>
        a. Lasso Regression
3. Model <br>
        a. Mord Ordinal Logistic Regression

The fitted pipeline is then serialized with joblib, served with Fast API (Uvicorn), containarized with Docker, and finally deployed to HuggingFace Spaces. 

Prediction requests can be sent to https://dkondic-ml-api.hf.space/predict as a list of dictionaries where each dictionary is an instance to predict. Thus, prediction is possible for single instance or batch of instances. Please see <a href="https://dkondic-ml-api.hf.space/">ML API Docs</a> for more indormation.<br> 

#### Request Body
```
[
  {
    "CUST_NBR": "string",
    "MENU_TYP_DESC": "string",
    "PYR_SEG_CD": "string",
    "DIV_NBR": "string",
    "WKLY_ORDERS": 0,
    "PERC_EB": 0,
    "AVG_WKLY_SALES": 0,
    "AVG_WKLY_CASES": 0
  }
]
```
#### Resonse Body
```
{
  "prediction": [
    0
  ]
}
```
#### Prediction xample using Python requests
```py
import requests

data = [
        {"CUST_NBR":"1111",
         "MENU_TYP_DESC":"MEXICAN",
         "PYR_SEG_CD":"Education",
         "DIV_NBR":"20",
         "WKLY_ORDERS": 15,
         "PERC_EB":0.80,
         "AVG_WKLY_SALES":2656.04,
         "AVG_WKLY_CASES":67.00}]

response = requests.post("https://dkondic-ml-api.hf.space/predict", json=data)
print(response.json())
```

