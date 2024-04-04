### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

quantidade= 40 
preco = 20 

if quantidade >  0 and preco > 0:
    print("Valores Validos")
else:
    print("Valores invalidos")

#outra forma 
quantidade = int(input("Digite a quantidade de valores:"))
preco = float(input("Digite o preço:"))

if quantidade > 0 and preco > 0:
    print("Valores Validos")
else:
    print("Valores Invalidos")

#com função 

def valores_produtos():
    quantidade = 20
    preco = 20
    if quantidade > 0 and preco >0:
        print("Valores Validos")
    else:
        print("Valores Invalidos")

valores_produtos()      

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

texto = " ola mundo estou aprendendo python "
palavras = texto.split(" ")
print(palavras)

contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra]=+1
    else:
        contagem_palavras[palavra] = 0   


