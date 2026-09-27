from pathlib import Path

import pandas as pd
import streamlit as st
import plotly.express as px
import openpyxl
import plotly


BASE_DIR = Path(__file__).resolve().parent
PAGES_DIR = BASE_DIR / "Pages"

pg = st.navigation([
    st.Page(PAGES_DIR / "Dadosdoprojeto.py", title="Dados do projeto"),
    st.Page(PAGES_DIR / "Analisequalitativa.py", title="Análise qualitativa"),
    st.Page(PAGES_DIR / "Analisequantitativa.py", title="Análise quantitativa"),
    st.Page(PAGES_DIR / "Conclusão.py", title="Conclusão"),
])

pg.run()
