#Exercício 6: crie um algoritmo usando while true para simular um menu interativo, se a opção for 1, print olá, se a opção for igual a 2, print sair

while True:
   opcao = int(input("Qual a opção desejada? "))
   if opcao == 1:
      print ("olá")
   elif opcao == 2:
      print("sair")
      break
   else:
      print("opção invalida, esoclha entre 1 ou 2")
      