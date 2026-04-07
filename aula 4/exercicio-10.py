# exercício 10 - crie um algoritmo para simular sistema com menu. o usuario pode cadastras, listar ou sair da estrtura.

# se opçao 1, solicite nome, idade, cidade e deixe estas informaçoes em uma estrutura de lista dentro de lista, 
# se opçao 2, print o respectivo nome, idade e cidade da pessoa, 
# se opçao 3, crie uma estrutura para sair do codigo

lista = []
opcao = 0
while opcao != 3:
 print("bem vindo! escolha a opção:")
 print("1 - cadastrar")
 print("2 - listar")
 print("3 - sair do programa")
 print("---------------------------------------")
 opcao = int(input(""))
 if opcao == 1:
  nome = str(input("digite seu nome: "))
  idade = str(input("digite sua idade: "))
  cidade = str(input("digite sua cidade: "))
  total = [nome,idade,cidade]

 elif opcao == 2:
  if len(lista) < 0:
   print("não há o que listar")
  else:
   print(f"nome: {nome}")
   print(f"idade: {nome}")
   print(f"cidade: {cidade}")
 else:
  print("opção invalida")