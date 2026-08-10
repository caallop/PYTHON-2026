#Exercício 8: crie um algoritmo para solicitar nome, porém mande apenas os nomes que forem >= 3 para a lista de nomes
lista = []
while True:
    nome = input("digite um nome: ")
    if len(nome) < 4:
        lista.append(nome)
        print(lista)
    elif len(nome) >= 4:
        print("digite um nome, com até 3 caracteres")

