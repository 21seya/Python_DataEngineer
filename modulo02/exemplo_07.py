try:
    num_1 = int(input("Inserir um numero inteiro :"))
    num_2 = int(input("Inserir outro numero inteiro :"))
    res = num_1 // num_2
    print(res)
except ZeroDivisionError:
    print("Error em fazer a divisão dos numeros")