#Crie um dicionario para armazenar informações de um livro. 
#incluindo titulo ,autor, e ano de publicação. Imprime cada informação. 

from typing import Dict,Any

livro: Dict[str,Any]={
    "Titulo":"Game of Thrones",
    "Autor":"Estagiario",
    "Ano":2023
}

lista_de_elementos = livro.items()
for elementos in lista_de_elementos:
    print(elementos)
