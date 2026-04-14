#xercício 7: crie um programa que solicite 5 numeros inteiros e decremente os valores inseridos pelo usuario
soma = 0
i = 0

while i < 5:
    num = int(input("Digite seu numero inteiro: "))
    soma -= num
    i += 1
    print(i)
    print(soma)