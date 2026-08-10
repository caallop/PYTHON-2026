#exercicio 14: crie um programa qie slicite nome, curso e idade de 3 pessoas, armazene cada pessoa como uma lista dentro de uma lista_completa

lista = []

while len(lista) < 3:
    idade = int(input("digite a idade: "))
    nome = input("digite o nome: ")
    curso = input("digite o curso: ")
    pessoa = [nome, idade, curso] 
    lista.append(pessoa)
    print(lista)
