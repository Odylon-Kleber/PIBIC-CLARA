import pandas as pd
from scipy.stats import mannwhitneyu


GABARITO_CONHECIMENTO = (
    "V", "V", "V", "V", "F", "V", "V", "V",
    "V", "V", "V", "V", "V", "V", "V", "V",
)
GABARITO_PERCEPCAO = tuple({"4", "5"} for _ in range(8))


def normalizar_resposta(valor):
    if pd.isna(valor):
        return ""
    resposta = str(valor).strip().upper()
    if resposta.endswith(".0") and resposta[:-2].isdigit():
        return resposta[:-2]
    return resposta


def pontuar_questionario(dataframe):
    if len(dataframe.columns) != 29:
        raise ValueError(
            "O questionário precisa conter 16 itens de conhecimento, "
            "8 itens de percepção e 5 colunas iniciais."
        )

    pontuado = dataframe.copy()
    pontuado.iloc[:, 0] = pontuado.iloc[:, 0].astype("string")
    coluna_participacao = pontuado.columns[4]
    colunas_conhecimento = list(pontuado.columns[5:21])
    colunas_percepcao = list(pontuado.columns[21:29])
    pontuado[coluna_participacao] = (
        pontuado[coluna_participacao]
        .map(normalizar_resposta)
        .eq("S")
        .astype(int)
    )
    pontos_conhecimento = pd.DataFrame(
        {
            coluna: pontuado[coluna]
            .map(normalizar_resposta)
            .eq(resposta)
            .astype(int)
            for coluna, resposta in zip(
                colunas_conhecimento,
                GABARITO_CONHECIMENTO,
            )
        },
        index=pontuado.index,
    )
    pontos_percepcao = pd.DataFrame(
        {
            coluna: pontuado[coluna]
            .map(normalizar_resposta)
            .isin(respostas)
            .astype(int)
            for coluna, respostas in zip(
                colunas_percepcao,
                GABARITO_PERCEPCAO,
            )
        },
        index=pontuado.index,
    )

    pontuado[colunas_conhecimento] = pontos_conhecimento
    pontuado[colunas_percepcao] = pontos_percepcao
    pontuado["Pontos participação prévia"] = pontuado[coluna_participacao]
    pontuado["Pontos conhecimento"] = pontos_conhecimento.sum(axis=1)
    pontuado["Pontos percepção"] = pontos_percepcao.sum(axis=1)
    pontuado["Pontos total"] = (
        pontuado["Pontos conhecimento"]
        + pontuado["Pontos percepção"]
        + pontuado["Pontos participação prévia"]
    )
    return pontuado


def comparar_pontuacoes(dados_pre, dados_pos):
    resultados = []
    for coluna in (
        "Pontos conhecimento",
        "Pontos percepção",
        "Pontos total",
    ):
        teste = mannwhitneyu(
            dados_pre[coluna],
            dados_pos[coluna],
            alternative="two-sided",
            method="auto",
        )
        resultados.append(
            {
                "Variável": coluna,
                "Mediana pré": dados_pre[coluna].median(),
                "Mediana pós": dados_pos[coluna].median(),
                "U": teste.statistic,
                "p-valor (bilateral)": teste.pvalue,
            }
        )
    return pd.DataFrame(resultados)
