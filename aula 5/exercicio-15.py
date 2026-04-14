#exercicio 15: Crie um programa que solicite numeros para o usuario pare quando digitar 0, armazene os nmeros em uma lista mostre a lista completa e a soma dos valores
lista = []
num = -1
soma = 0
while num != 0:
    num = int(input("digite seu numero(para sair digite 0): "))
    if num == 0:
        continue
    soma += num
    
    lista.append(num)
print(lista)
print(f"a soma total dos numeros foi {soma}")