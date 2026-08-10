#Exercício 12: criar um programa a qual ao selecionar opção 1, solicita e envia nomes para uma lista de nomes, se 2, solicia e envia os cpfs para uma lista, se 3, solicida e envia a idade para uma lista e depois adicione tudo par auma lista com total
lista_nome = []
lista_idade = []
lista_cpf = []
lista_geral = []

while True:
   print("1. adicionar nome")
   print("2. adicionar cpf")
   print("3. adicionar idade")
   print("4. sair")
   opcao =  input("digite um numero: ")
   if opcao == "1":
      nome = input("qual nome deseja adicionar a lista: ")
      lista_nome.append(nome)
      lista_geral.append(nome)
   elif opcao == "2":
      cpf = input("qual cpf deseja adicionar a lista: ")
      lista_cpf.append(cpf)
      lista_geral.append(cpf)
   elif opcao == "3":
      idade = input("qual idade deseja adicionar a lista: ")
      lista_idade.append(idade)
      lista_geral.append(idade)
   elif opcao == "4":
      print (lista_geral)
      break