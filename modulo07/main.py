from etl import filtrar_produtos_nao_entregues, ler_csv, soma_valores_produtos

path_arquivo = "vendas.csv"

lista_produtos = ler_csv(path_arquivo)
produto_entregues = filtrar_produtos_nao_entregues(lista_produtos)
valor_soma_produtos = soma_valores_produtos(produto_entregues)
print(valor_soma_produtos)
