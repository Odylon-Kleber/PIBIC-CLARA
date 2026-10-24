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

# Dados pré intervenção
st.text("PRÉ INTERVENÇÃO")
dados_PRÉ_INTERVENÇÃO = pd.read_excel(
    PROJECT_DIR / "pre_intervencao.ods",
    engine="odf",
)
dados_PRÉ_INTERVENÇÃO
# Dados pós intervenção
st.text("PÓS INTERVENÇÃO")
dados_PÓS_INTERVENÇÃO = pd.read_excel(
    PROJECT_DIR / "pos_intervencao.ods",
    engine="odf",
)
dados_PÓS_INTERVENÇÃO


def mostrar_graficos_frequencia(dataframe, prefixo_chave):
    variaveis_analise = [
        coluna for coluna in dataframe.columns
        if str(coluna).strip().casefold() not in {"participante", "participante:"}
    ]

    if dataframe.empty:
        st.warning("Não há dados disponíveis para gerar os gráficos.")
        return

    colunas_graficos = st.columns(2)
    for indice, coluna in enumerate(variaveis_analise):
        respostas = dataframe[coluna].map(
            lambda valor: (
                "Não informado"
                if pd.isna(valor) or str(valor).strip() in {"", "-"}
                else str(valor).strip()
            )
        )
        frequencia = respostas.value_counts().rename_axis("Resposta").reset_index(
            name="Frequência"
        )
        frequencia["Frequência relativa (%)"] = (
            frequencia["Frequência"] / len(dataframe) * 100
        )

        grafico = px.bar(
            frequencia,
            x="Frequência relativa (%)",
            y="Resposta",
            orientation="h",
            text="Frequência relativa (%)",
            hover_data={"Frequência": True, "Frequência relativa (%)": ":.1f"},
            title="Frequência relativa (%)",
        )
        grafico.update_traces(
            texttemplate="%{x:.1f}%",
            textposition="outside",
            cliponaxis=False,
        )
        grafico.update_layout(
            xaxis_title="Participantes (%)",
            yaxis_title=None,
            xaxis_range=[0, min(110, frequencia["Frequência relativa (%)"].max() + 10)],
            margin=dict(l=10, r=20, t=55, b=30),
            height=max(280, 55 * len(frequencia)),
        )

        with colunas_graficos[indice % 2]:
            st.markdown(f"**{str(coluna).strip()}**")
            st.plotly_chart(
                grafico,
                width="stretch",
                key=f"frequencia_{prefixo_chave}_{indice}",
            )


st.header("ANÁLISE DESCRITIVA PRÉ-INTERVENÇÃO")
mostrar_graficos_frequencia(dados_PRÉ_INTERVENÇÃO, "pre")

st.header("ANÁLISE DESCRITIVA PÓS-INTERVENÇÃO")
mostrar_graficos_frequencia(dados_PÓS_INTERVENÇÃO, "pos")
