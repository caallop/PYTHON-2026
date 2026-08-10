# exercício 4 - some a media de valores digitados pelo usuario. crie um algoritmo para solicitar 5 valores nao intieros , isira em uma lista. após isso, crie uma estrutura para somar e retornar a media dos elementos dessa lista


lista = []
soma = 0
for i in range(1, 6):
    numeros = float(input("digite um numero: "))
    lista.append(numeros)
    print(lista)

    soma += numeros
    print(soma)
print(soma / len(lista))
