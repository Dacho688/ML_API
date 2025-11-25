# -*- coding: utf-8 -*-

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
