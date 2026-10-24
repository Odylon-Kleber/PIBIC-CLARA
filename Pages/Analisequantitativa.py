from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px
import openpyxl
import plotly
import unicodedata
from pontuacao import comparar_pontuacoes, pontuar_questionario


# Configurações da página
st.set_page_config(
    page_title="AnalisaMed",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

PROJECT_DIR = Path(__file__).resolve().parent.parent
LOGO_PATH = PROJECT_DIR / "imagem" / "logomarca.png"
st.sidebar.image(str(LOGO_PATH), caption="AnalisaMed")

st.sidebar.write("Odylon Kleber Pereira de Souza")
st.sidebar.write("© 2026 AnalisaMed. Todos os direitos reservados.")


# Dados pré intervenção
df_pré_intervenção = pd.read_excel(
    PROJECT_DIR / "pre_intervencao.ods",
    engine="odf",
)
# Dados pós intervenção
df_pós_intervenção = pd.read_excel(
    PROJECT_DIR / "pos_intervencao.ods",
    engine="odf",
)


df_pré_intervenção = pontuar_questionario(df_pré_intervenção)
df_pós_intervenção = pontuar_questionario(df_pós_intervenção)

st.text("PRÉ INTERVENÇÃO")
st.caption(
    "Nas colunas dos itens, 1 indica resposta conforme o gabarito e 0 indica "
    "resposta diferente ou em branco. A pergunta 00 também é pontuada: "
    "S = 1 e N, '-' ou resposta em branco = 0. Esse ponto é incluído na "
    "coluna 'Pontos participação prévia' e em 'Pontos total'."
)
st.dataframe(df_pré_intervenção, width="stretch")
st.text("PÓS INTERVENÇÃO")
st.dataframe(df_pós_intervenção, width="stretch")

st.header("Teste de Mann–Whitney")
resultados = comparar_pontuacoes(
    df_pré_intervenção,
    df_pós_intervenção,
)
st.dataframe(resultados, width="stretch", hide_index=True)
