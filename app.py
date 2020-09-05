import requests
import json
import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go

#urls
LTN = "https://apiapex.tesouro.gov.br/aria/v1/sistd/custom/historico?ano=2020&idSigla=2"
LFT = "https://apiapex.tesouro.gov.br/aria/v1/sistd/custom/historico?ano=2020&idSigla=1"
NTNB_p= "https://apiapex.tesouro.gov.br/aria/v1/sistd/custom/historico?ano=2020&idSigla=5"
IPCA = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.16121/dados?formato=json'

def dolar():
    y = requests.get('https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados?formato=json').content
    yy = json.loads(y)
    dolar = pd.DataFrame(yy)
    dolar['data'] = pd.to_datetime(dolar['data'],dayfirst=True)
    dolar = dolar.sort_values('data')
    dolar = dolar[dolar['data']>'01/01/2020']
    dolar_plot = px.line(data_frame=dolar,x='data',y='valor')
    return dolar_plot
def ipca():
    y = requests.get(IPCA).content
    yy = json.loads(y)
    dolar = pd.DataFrame(yy)
    dolar['data'] = pd.to_datetime(dolar['data'],dayfirst=True)
    dolar = dolar.sort_values('data')
    dolar = dolar[dolar['data']>'01/01/2020']
    dolar_plot = px.line(data_frame=dolar,x='data',y='valor')
    return dolar_plot

#def plot_titulo(url):
#    titulo=pd.ExcelFile(url)
#    titulo_df =titulo.parse(0,header=[1])
#    fig = go.Figure()
#    for i in titulo_df.columns[1:]:
#        fig.add_trace(go.Scatter(x=titulo_df['Dia'],y=titulo_df[f'{i}'],name=f'{i}'))
#    return fig

def main():
    #dolar()
    dolar_plot = dolar()
    st.markdown("<h1 style='text-align: center; color: Black;'>Dolar</h1>", unsafe_allow_html=True)
    st.write(dolar_plot)
    ipca_plot = ipca()
    st.markdown("<h1 style='text-align: center; color: Black;'>IPCA</h1>", unsafe_allow_html=True)
    st.write(ipca_plot)


    #ltn = plot_titulo(LTN)
    #st.markdown("<h1 style='text-align: center; color: Black;'>LTN</h1>", unsafe_allow_html=True)
    #st.write(ltn)
    #select = st.selectbox('Qual título você deseja visualizar?',['','LTN','LFT','NTNB Principal'])
    #if select == 'LTN':
    #    ltn = plot_titulo(LTN)
    #    st.markdown("<h1 style='text-align: center; color: Black;'>LTN</h1>", unsafe_allow_html=True)
    #    st.write(ltn)
    #elif select == 'LFT':
    #    lft = plot_titulo(LFT)
    #    st.markdown("<h1 style='text-align: center; color: Black;'>LFT</h1>", unsafe_allow_html=True)
    #    st.write(lft)
    #elif select == 'NTNB Principal':
    #    ntnb_p = plot_titulo(NTNB_p)
    #    st.markdown("<h1 style='text-align: center; color: Black;'>NTNB Principal</h1>", unsafe_allow_html=True)
    #    st.write(ntnb_p)
    #else:
    #    pass

if __name__=='__main__':
    main()