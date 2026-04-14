realizado = False


while not realizado:
    entrada = int(input("insira alguma coisa: "))
    if entrada == 999:
        realizado = True
    else:
        print(entrada)
