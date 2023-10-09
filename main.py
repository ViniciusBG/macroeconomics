from typing import Union
from src.utils import *
import json
import requests

from fastapi import FastAPI

app = FastAPI()


@app.get("/test")
def read_root():
    return {"Hello World"}

@app.get("/data")
def get_data(url= "http://api.bcb.gov.br/dados/serie/bcdata.sgs.16121/dados?formato=json"):
    request = requests.get(url).content
    json_request = json.loads(request)
    return json_request

@app.get("/test_json")
def test_json():
    my_dict = {}

    # Populate the dictionary with 10 keys, each mapped to a list of 10 values
    for i in range(10):
        key = f'key_{i}'
        values = [f'value_{i}_{j}' for j in range(10)]
        my_dict[key] = values

    # Print the dictionary
    return my_dict
