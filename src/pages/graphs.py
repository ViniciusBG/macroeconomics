import streamlit as st
from omegaconf import OmegaConf

from utils.utils import download_data, plot




conf = OmegaConf.load("globals.yaml")

st.set_page_config(page_title="Plotting Demo", page_icon="📈")




def main():
    st.sidebar.header("Gráficos")

    source = st.sidebar.selectbox(
        "Quais dados você gostaria de ver?", (conf["Sources"].keys())
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

    st.write(source)

    df = download_data(conf["Sources"][source], data)

    if output_format == "Tabela":
        st.dataframe(df)
    else:
        graph = plot(df)
        st.write(graph)


if __name__ == "__main__":
    main()
