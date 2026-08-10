#exercicio 10: criar um programa que solicite 5 nomes e insira em uma lista
lista = []

while len(lista) < 5:
     print(len(lista))
     nome = input('digite o nome: ')
     lista.append(nome)
print(lista)