import streamlit as st
import requests
import json
import pandas as pd 

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Vinicius Gomes")

# st.sidebar.success("Select a demo above.")

st.markdown(
    """
    It took a lot of time for me to discover what I am/like to be. 
    I believe the term "full stack" data scientist is the best term for it (as weird as it may sound)!

    I'm a Data Scientist with  data engineering skills who is fascinated by creating end-to-end projects, 
    explainable machine learning models, and predicting human behaviour.

    Most familiar languages and tools:

    1) Languages : Python, SQL\n
    2) WebScrapping: Selenium, BeatifulSoup\n
    3) Data Processing : Pandas, Numpy, Scipy, NLTK\n
    4) Modelling/Machine Learning : Scikit-learn, XGBoost, Statsmodels\n
    5) Deep learning: Keras, Tensorflow\n
    6) NLP: NLTK, BERT\n
    7) Data Visualisation : Matplotlib, Seaborn, Plotly, Altair\n
    8) Business intelligence: Metabase, Google Data Studio, Power BI\n
    9) Monitoring experiments: MLFlow\n
    10) Deployment: FastAPI,Streamlit, Flask, Gradio, Docker

    """  # noqa
)


def call_api():
    response = requests.get("http://fastapi:80/test").content
    return json.loads(response)

st.write(f"### Results from the API: {call_api()}")



def call_api_json():
    response = requests.get("http://fastapi:80/test_json").content
    return json.loads(response)




def download_data(url="http://api.bcb.gov.br/dados/serie/bcdata.sgs.16121/dados?formato=json"):
    request = requests.get(url).json()
    json_request = json.loads(request)
    json_request = json_request.json()
    return json_request

st.write(pd.DataFrame(call_api_json()))