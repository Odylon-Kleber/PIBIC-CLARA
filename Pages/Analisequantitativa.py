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