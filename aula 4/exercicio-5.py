# exercício 5 - crie uma estrutura para solicitar 10 numeros para o usuario, apos isso crie duas listas (impar e par) e insita os valores pares na lista oar e os valores impar, nas listas impar. print lista completa, lista par e lista impar.
lista = []
lista_par = []
lista_impar = []
for i in range(1, 11):
    numeros = int(input("digite um numero: "))
    if numeros % 2 == 0:
        lista_par.append(numeros)
    else:
        lista_impar.append(numeros)
    lista.append(numeros)

print(lista)
print(lista_impar)
print(lista_par)
