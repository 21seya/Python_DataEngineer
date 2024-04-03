try:
    resultado = len(3)
    print(resultado)

except TypeError as e:
    print(e)
else:
    print("Tudo ocorreu bem")    
finally:
    print("Aprendizado constante")    