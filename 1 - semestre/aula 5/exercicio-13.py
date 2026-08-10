#exercicio 13:crie um programa que solicite 5 números inteiros, armazene em uma lista seu valor ao quadrado. [numero, numero**2]

lista = []
numquad = 0 

while len(lista) < 5:
    num = int(input("digite o numero: "))
    numquad = num**2
    lista2 = [num, numquad] 
    lista.append(lista2)
    print(lista)
