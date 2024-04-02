nome = input("Digite o seu nome :")
qtd_caracteres = len(nome)
print(" A quantidade de caracteres e",qtd_caracteres)

BONUS_CONSTANTE = 1000

# 2) Solicita ao usuário que digite seu nome

nome = input("Digite o seu nome :")
print(nome)

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

salario = float(input("Digite o  seu salario :"))
print(salario)

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

bonus = float(input("Digite o seu bonus :"))


# 4) Calcule o valor do bônus final

valor_bonus =  BONUS_CONSTANTE + salario * bonus 
print(f"O usuario {nome} possui o bonus de ",{valor_bonus})

# 5) Imprima cálculo do KPI para o usuário
print()


