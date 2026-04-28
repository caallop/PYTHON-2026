#Exercício 10: vamos criar um sistemas de menu simples

#1. adicionar numero
#2. remover ultimo numero
#3. mostrar lista
#4. sair


lista = []

while True:
   print("1. adicionar numero")
   print("2. remover ultimo numero")
   print("3. mostrar lista")
   print("4. sair")
   opcao =  input("digite um numero: ")
   if opcao == "1":
      nmr = int(input("qual numero deseja adicionar a lista: "))
      lista.append(nmr)
   elif opcao == "2":
      lista.pop()
   elif opcao == "3":
      print(lista)
   elif opcao == "4":
      break