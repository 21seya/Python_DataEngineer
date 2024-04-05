from typing import Dict 

produto:Dict[str,any]

import json

produto:dict = {
    "nome":"Sapato",
    "tamanho":39,
    "preco":50.00,
    "Disponibilidade":True
}

lista_produtos : list = []

lista_produtos.append(produto)

carrinho_json = json.dumps(lista_produtos)
print(carrinho_json)


