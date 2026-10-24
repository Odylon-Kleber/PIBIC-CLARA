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

PROJECT_DIR = Path(__file__).resolve().parent.parent
LOGO_PATH = PROJECT_DIR / "imagem" / "logomarca.png"
st.sidebar.image(str(LOGO_PATH), caption="AnalisaMed")
st.sidebar.write("Odylon Kleber Pereira de Souza")
st.sidebar.write("© 2026 AnalisaMed. Todos os direitos reservados.")

# Título do dashboard
st.markdown('# 📊 ANÁLISE DE DADOS')
st.header("Título do projeto")
st.text("Educação em saúde sexual e reprodutiva para adolescentes: diálogo entre a universidade e estudantes de escolas públicas de Marabá.", text_alignment="justify")
st.header("Objetivo Geral")
st.text("Informar estudantes da rede pública de ensino sobre saúde reprodutiva e sexual da mulher nas áreas de contracepção, planejamento familiar, prevenção de ISTs e saúde menstrual.", text_alignment="justify")
st.header("Objetivos Específicos")
st.text("Comparar os questionários e a aquisição desse novo conhecimento entre as jovens.")
st.header("Método")
st.text("Trata-se de um estudo quantitativo, quase-experimental, do tipo pré e pós-intervenção, realizado com aproximadamente 100 alunas do 2º e 3º ano do ensino médio de quatro escolas públicas do município de Marabá. A intervenção será realizada por meio de palestra educativa expositivo-dialogada, com espaço para esclarecimento de dúvidas.", text_alignment="justify")
# Banco de dados
st.header('Banco de dados')
# Dados pré intervenção
st.text("PRÉ INTERVENÇÃO")
dados_PRÉ_INTERVENÇÃO = pd.read_excel(
    PROJECT_DIR / "pre_intervencao.ods",
    engine="odf",
)
dados_PRÉ_INTERVENÇÃO
df = dados_PRÉ_INTERVENÇÃO
# Dados pós intervenção
st.text("PÓS INTERVENÇÃO")
dados_PÓS_INTERVENÇÃO = pd.read_excel(
    PROJECT_DIR / "pos_intervencao.ods",
    engine="odf",
)
dados_PÓS_INTERVENÇÃO
df = dados_PÓS_INTERVENÇÃO
