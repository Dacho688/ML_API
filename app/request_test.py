# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 17:00:22 2025

@author: dkondic
"""
import requests

data = [
        {"CUST_NBR":"1111",
         "MENU_TYP_DESC":"MEXICAN",
         "PYR_SEG_CD":"Education",
         "DIV_NBR":"20",
         "WKLY_ORDERS": 1,
         "PERC_EB":0.80,
         "AVG_WKLY_SALES":2656.04,
         "AVG_WKLY_CASES":67.00}]

response = requests.post("http://localhost:7860/predict", json=data)
print(response.json())
