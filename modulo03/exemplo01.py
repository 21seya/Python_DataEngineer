lista_alunos = ['Lucia','Camila','Vitoria']

for alunos in lista_alunos:
    print(alunos)


texto = " ola mundo estou aprendendo python "
palavras = texto.split(" ")
print(palavras)

contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra]=+1
    else:
        contagem_palavras[palavra] = 0      