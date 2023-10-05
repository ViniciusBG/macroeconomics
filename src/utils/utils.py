import requests
import json
import pandas as pd
import plotly.express as px


def download_data(url, data_inicio):
    request = requests.get(url).content
    json_request = json.loads(request)

    dataframe = pd.DataFrame(json_request)
    dataframe["data"] = pd.to_datetime(dataframe["data"], dayfirst=True)

    filtered_data = dataframe[dataframe["data"] > data_inicio]
    sorted_dataframe = filtered_data.sort_values("data")

    return sorted_dataframe


def plot(data):
    plot = px.line(data_frame=data, x="data", y="valor")
    plot = plot.update_yaxes(rangemode="tozero")

    return plot
