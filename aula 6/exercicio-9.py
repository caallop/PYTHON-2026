#Exercício 9: crie um algoritmo com listas de notas validos. se -1 pare a estrutura, se nota >0 ou nota < 10 coninue, ao final, calcule a media das notas
lista = []
soma = 0
while True:
   nmr =  int(input("digite um numero "))
   if nmr > 0 and nmr <= 10:
      soma += nmr
      lista.append(nmr)
      print(f"a soma total é: {soma}")
   elif nmr > 10:
      print("digite um numero de 0 até 10")
   else:
      print(f"a lista final é: {lista}")
      print(f"a media final é: {len(lista)}")
      break