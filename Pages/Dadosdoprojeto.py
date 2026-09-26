from pathlib import Path

import pandas as pd
import streamlit as st
import plotly.express as px
import openpyxl
import plotly


# Configurações da página
st.set_page_config(
    page_title="AnalisaMed",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

LOGO_PATH = Path(__file__).resolve().parent.parent / "imagem" / "logomarca.png"
st.sidebar.image(str(LOGO_PATH), caption="AnalisaMed")
st.sidebar.write("Odylon Kleber Pereira de Souza")
st.sidebar.write("© 2026 AnalisaMed. Todos os direitos reservados.")

# Título do dashboard
st.markdown('# 📊 ANÁLISE DE DADOS')
st.header("Título do projeto:")
st.text("Educação em saúde sexual e reprodutiva para adolescentes: diálogo entre a universidade e estudantes de escolas públicas de Marabá", text_alignment="justify")
st.header("Objetivo Geral:")
st.text("Informar estudantes da rede pública de ensino sobre saúde reprodutiva e sexual da mulher nas áreas de contracepção, planejamento familiar, prevenção de ISTs e saúde menstrual.", text_alignment="justify")
st.header("Objetivos Específicos:")
st.text("Comparar os questionários e a aquisição desse novo conhecimento entre as jovens")
# Banco de dados
st.header('Banco de dados')

dados_ANISIO = pd.read_excel("ANISIO.xlsx")
dados_ANISIO
df = dados_ANISIO