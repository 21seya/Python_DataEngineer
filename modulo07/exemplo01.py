valor_1 = 10
valor_2 = 30


def soma(valor_1: float, valor_2: float) -> float:
    """
    Função simples de soma de dados
    """
    valor_3 = valor_1 + valor_2
    return valor_3


dados = soma(valor_1, valor_2)
print(dados)


def multiplicar(valor_1: int, valor_2: int) -> int:
    """
    Função pra multiplicar dados
    """
    valor_3 = valor_1 * valor_2
    return valor_3


dados_mul = multiplicar(valor_1, valor_2)
print(dados_mul)
