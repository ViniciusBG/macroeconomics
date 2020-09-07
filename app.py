import requests
import json
import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go

#urls
DOLAR = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados?formato=json'
IPCA = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.16121/dados?formato=json'

def plot(ativo,data_inicio):
    y = requests.get(ativo).content
    yy = json.loads(y)
    dolar = pd.DataFrame(yy)
    dolar['data'] = pd.to_datetime(dolar['data'],dayfirst=True)
    dolar = dolar.sort_values('data')
    dolar = dolar[dolar['data']>data_inicio]
    dolar_plot = px.line(data_frame=dolar,x='data',y='valor')
    return dolar_plot



def main():
    #dolar()
    st.sidebar.header("Gráficos")
    select = st.sidebar.selectbox("Qual gráfico você gostaria de ver?",("Dolar", "IPCA"))
    st.sidebar.text("Desenvolvido por Vinicius B Gomes")
    if select == 'Dolar':
        dolar_plot = plot(DOLAR,'01/01/2020')
        st.markdown("<h1 style='text-align: center; color: Black;'>Dolar</h1>", unsafe_allow_html=True)
        st.write(dolar_plot)
    if select == 'IPCA':
        ipca_plot = plot(DOLAR,'01/01/2020')
        st.markdown("<h1 style='text-align: center; color: Black;'>IPCA</h1>", unsafe_allow_html=True)
        st.write(ipca_plot)




if __name__=='__main__':
    main()
