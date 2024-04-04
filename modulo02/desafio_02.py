


# 2) Solicita ao usuário que digite seu nome
nome_usuario = input("Digite o seu nome :")

if nome_usuario.isdigit():
    print("Você digitou seu nome errado!!!")
    exit()
elif len(nome_usuario) == 0:
    print("Você não digitou seu nome errado!!")
    exit()
elif nome_usuario.isspace():
    print("Você não digitou nada")
    exit()
