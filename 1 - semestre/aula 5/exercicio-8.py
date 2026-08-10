#Exercício 8: crie um prgrama para gerar uma taboada, a partir de duas variaveis, (numero limite)
i = 1
num = int(input("digite o numero que voce quer saber a taboada: "))
while i <= 10:
    mult = i * num
    print(f"{num} X {i} = {mult}")
    i += 1
