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

# Banco de dados
dados_ANISIO = pd.read_excel(PROJECT_DIR / "ANISIO.xlsx")
dados_JOSE_CURSINHO = pd.read_excel(PROJECT_DIR / "JOSE_CURSINHO.xlsx")
dados_PEQUENO_PRINCIPE = pd.read_excel(PROJECT_DIR / "PEQUENO_PRINCIPE.xlsx")
# Dados unificados
df_unificado_pre = pd.concat([dados_ANISIO, dados_JOSE_CURSINHO, dados_PEQUENO_PRINCIPE], ignore_index=True)
df_unificado_pos = pd.concat([dados_ANISIO, dados_JOSE_CURSINHO, dados_PEQUENO_PRINCIPE], ignore_index=True)


def mostrar_graficos_frequencia(dataframe, prefixo_chave):
    variaveis_analise = [
        coluna for coluna in dataframe.columns
        if coluna.strip().casefold() not in {"participante", "participante:"}
    ]
    colunas_graficos = st.columns(2)

    for indice, coluna in enumerate(variaveis_analise):
        respostas = dataframe[coluna].map(
            lambda valor: (
                "Não informado"
                if pd.isna(valor) or str(valor).strip() in {"", "-"}
                else str(valor).strip()
            )
        )
        frequencia = respostas.value_counts().rename_axis("Resposta").reset_index(name="Frequência")
        frequencia["Frequência relativa (%)"] = (
            frequencia["Frequência"] / len(dataframe) * 100
        )
        opcoes_resposta = None
        if any(
            questao in coluna
            for questao in (
                "06. Considero importante o uso de preservativos nas relações sexuais.",
                "07. A falta de informação pode aumentar o risco de ISTs",
            )
        ):
            opcoes_resposta = [str(valor) for valor in range(1, 6)]
            respostas_presentes = set(frequencia["Resposta"])
            ausentes = [
                {"Resposta": resposta, "Frequência": 0, "Frequência relativa (%)": 0}
                for resposta in opcoes_resposta
                if resposta not in respostas_presentes
            ]
            if ausentes:
                frequencia = pd.concat(
                    [frequencia, pd.DataFrame(ausentes)],
                    ignore_index=True,
                )

        grafico = px.bar(
            frequencia,
            x="Frequência relativa (%)",
            y="Resposta",
            orientation="h",
            text="Frequência relativa (%)",
            hover_data={"Frequência": True, "Frequência relativa (%)": ":.1f"},
            title="Frequência relativa (%)",
            category_orders=(
                {"Resposta": opcoes_resposta}
                if opcoes_resposta is not None
                else None
            ),
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
            st.markdown(f"**{coluna.strip()}**")
            st.plotly_chart(
                grafico,
                width="stretch",
                key=f"frequencia_{prefixo_chave}_{indice}",
            )


st.header("ANÁLISE DESCRITIVA PRÉ-INTERVENÇÃO")
mostrar_graficos_frequencia(df_unificado_pre, "pre")

st.header("ANÁLISE DESCRITIVA PÓS-INTERVENÇÃO")
mostrar_graficos_frequencia(df_unificado_pos, "pos")