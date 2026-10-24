from pathlib import Path
import streamlit as st
import pandas as pd
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


dados_pre = pontuar_questionario(
    pd.read_excel(PROJECT_DIR / "pre_intervencao.ods", engine="odf")
)
dados_pos = pontuar_questionario(
    pd.read_excel(PROJECT_DIR / "pos_intervencao.ods", engine="odf")
)
resultados = comparar_pontuacoes(dados_pre, dados_pos)

st.header("Conclusão")
st.write(
    f"Foram analisados {len(dados_pre)} questionários pré-intervenção e "
    f"{len(dados_pos)} pós-intervenção. As medianas dos pontos de conhecimento "
    f"foram {resultados.loc[0, 'Mediana pré']:g} e "
    f"{resultados.loc[0, 'Mediana pós']:g}; de percepção, "
    f"{resultados.loc[1, 'Mediana pré']:g} e "
    f"{resultados.loc[1, 'Mediana pós']:g}; e de pontuação total, "
    f"{resultados.loc[2, 'Mediana pré']:g} e "
    f"{resultados.loc[2, 'Mediana pós']:g}, respectivamente. A pontuação total "
    "inclui os 16 itens de conhecimento, os 8 de percepção e a pergunta 00 "
    "(1 ponto para S; 0 para N, '-' ou resposta em branco; máximo de 25 pontos)."
)

for _, resultado in resultados.iterrows():
    significativa = resultado["p-valor (bilateral)"] < 0.05
    interpretacao = (
        "diferença estatisticamente significativa"
        if significativa
        else "não foi detectada diferença estatisticamente significativa"
    )
    st.write(
        f"{resultado['Variável']}: U = {resultado['U']:g}, "
        f"p = {resultado['p-valor (bilateral)']:.3g}; {interpretacao} "
        f"(mediana pré = {resultado['Mediana pré']:g}; "
        f"mediana pós = {resultado['Mediana pós']:g})."
    )