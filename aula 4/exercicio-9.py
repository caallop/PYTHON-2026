# exercício 9 - crie um algoritmo para solicitar nome e nota para 4 alunos. insira em uma estrutura com lista dentro de lista (nome, nota). após isso, crie uma estrutura para mostrar os alunaos aprovados com nota maior ou igual a 6, mostrando o respectivo nome e nota, crie tambem uma estrutura para mostrar os alnos com nota menor do que 6 e mostre o nome e nota

lista_aprovados = []
lista_reprovados = []

for i in range(1, 5):
    nome = str(input("qual nome? "))
    nota = int(input("qual a nota? "))
    nome_nota = [nome, nota]
    if nota >= 6:
        lista_aprovados.append(nome_nota)
    else:
        lista_reprovados.append(nome_nota)

print(f"os alunos reprovados foram: {lista_reprovados}")
print(f"os alunos aprovados foram: {lista_aprovados}")
