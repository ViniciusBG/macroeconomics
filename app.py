import requests
import json
import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go
from omegaconf import OmegaConf

conf = OmegaConf.load("globals.yaml")


def main():

    st.sidebar.header("Gráficos")
    source = st.sidebar.selectbox(
        "Qual gráfico você gostaria de ver?", (conf["Sources"].keys())
    )
    data = st.sidebar.selectbox(
        "Qual a data de início?",
        (conf["AVAILABLE_YEARS"]),
    )
    output_format = st.sidebar.selectbox(
        "O que você deseja ver?",
        (conf["OUTPUTS"]),
    )
    st.sidebar.text("Desenvolvido por Vinicius B Gomes")

    df = download_data(source,data)

    if output_format == "Tabela":
        st.dataframe(df)
    else:
        graph = plot(df)
        st.write(graph)


def download_data(ativo, data_inicio):

    url = conf["Sources"][ativo]

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


if __name__ == "__main__":
    main()
