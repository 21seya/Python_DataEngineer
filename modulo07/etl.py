import csv

path_arquivo = "vendas.csv"


def ler_csv(nome_arquivo_csv: str) -> list[dict]:
    """
    Função ler arquivo csv e retornar uma lista
    """
    lista = []
    with open(nome_arquivo_csv, mode="r", encoding="utf-8") as arquivo:
        ler_dados = csv.DictReader(arquivo)
        for linha in ler_dados:
            lista.append(linha)
    return lista


vendas_itens = list[dict]

vendas_itens = ler_csv(path_arquivo)
print(vendas_itens)


def filtrar_produtos_nao_entregues(lista: list[dict]) -> list[dict]:
    """
    Função que filtra os produtos = True
    """
    lista_produtos_filtrados = []
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_produtos_filtrados.append(produto)
    return lista_produtos_filtrados


def soma_valores_produtos(lista_produtos_filtrados: list[dict]) -> int:
    """
    Soma todos os produtos que estão na lista
    """
    valor_total = 0
    for produto in lista_produtos_filtrados:
        valor_total += int(produto.get("price"))
    return valor_total


lista_produtos = ler_csv(path_arquivo)
produto_entregues = filtrar_produtos_nao_entregues(lista_produtos)
print(produto_entregues)
