import glob
import os

import pandas as pd


# função que extrai os dados em json
def extrair_dados(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, "*.json"))
    df_lista = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_lista, ignore_index=True)
    return df_total


# função que transforma
def transformar_dados(df: pd.DataFrame):
    df["Receita"] = df["Quantidade"] * df["Venda"]
    return df


# função que carrega os dados
def carregar_dados(df: pd.DataFrame, formato_saida: list):
    for formato in formato_saida:
        if formato == "csv":
            df.to_csv("dados.csv", index=False)
        if formato == "parquet":
            df.to_parquet("dados.parquet", index=False)


# funcao pra criação de pipeline
def pipeline(pasta: str, formato_saida: list):
    dados_extraidos = extrair_dados(pasta)
    dados_calculados = transformar_dados(dados_extraidos)
    carregar_dados(dados_calculados, formato_saida)


# if __name__ == "__main__":
#    pasta : str = 'data'
#    dados_extraidos = extrair_dados(path=pasta)
#    dados_calculados = transformar_dados(dados_extraidos)
#    formato_saida: list = ["csv","parquet"]
#    dados_consolidados = carregar_dados(dados_calculados,formato_saida)
