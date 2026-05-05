 
#Exercício 1: crie uma estrtura com try/except para converter temperaturatura celcius em fahreinht

#fahreinht = (celcius * 9/5) + 32

try:
    celcius = float(input("Digite a temperatura em celcius "))
    fahreinht = (celcius * 9/5) + 32
    print(fahreinht)
except ValueError:
    print("Digite um valor numerico.")