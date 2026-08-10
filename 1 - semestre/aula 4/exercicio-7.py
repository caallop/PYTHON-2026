# exercício 7 - vamos fazer um algoritmo para cafastro com media, solicite 3 informaçoes, nome, nota 1 e nota 2 trez vezes, apos isso calcule a media de cada aluno e retorne uma lista contendo nome, nota1, nota2, media d ecada aluno


lista = []
k = 0
for i in range(3):
    nome = str(input("digite um nome: "))
    nota1 = float(input("digite a primeira nota: "))
    nota2 = float(input("digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    informacoes = [nome, nota1, nota2, media]
    lista.append(informacoes)

    k = k + 1
print(lista)
