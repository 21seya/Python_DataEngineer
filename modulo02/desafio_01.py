import math
# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
num_1 = int(input("Inserir um numero inteiro :"))
num_2 = int(input("Inserir outro numero inteiro :"))
res = num_1 // num_2
print(res)
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = float(input("Digite o raio :"))
area = math.pi * raio ** 2
print(f"{area:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Insira uma data no formato dd/mm/aaaa :")

data_usuario = "01/02/2002"
lista_dia_mes_ano = data_usuario.split("/")
print(f"O elemento 1 e 0 :{lista_dia_mes_ano[0]}")
print(f"O elemento 1 e 0 :{lista_dia_mes_ano[1]}")
print(f"O elemento 1 e 0 :{lista_dia_mes_ano[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
