# exercício 6 - crie um algoritmo para cadastro de alunos osnde deve ser solicitado nome e idade 5 vezes, porem a informaçao deve aparecer com lista dentro de lista, ou seja: [nome 1, idade1], [nome2, idade2],.., e assim por diante,print lista final.

# lista = [[],[],[],[],[]]
# k = 0
# for i in range (5):
#     nome = str(input("digite um nome: "))
#     idade = int(input("digite um idade: "))

#     lista[k].append(nome)
#     lista[k].append(idade)
#     k = k + 1
# print(lista)

## metodo do professor e que deve ser seguido. ------>

lista = []
for i in range(5):
    nome = str(input("digite um nome: "))
    idade = int(input("digite um idade: "))
    nome_idade = [nome, idade]
    lista.append(nome_idade)
print(lista)
