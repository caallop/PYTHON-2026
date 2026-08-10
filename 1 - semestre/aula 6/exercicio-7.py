#Exercício 7: crie um alguritmo usando while true para ignorar valores negativos. se o numero for 0, quebre a estrutura de repetição caso contrario, envie cada numero para uma lista

lista = []

while True:
    nmr = int(input("Digite o numero: "))
    if nmr < 0:
       print("invalido")
    elif nmr == 0:
        break
    else:
          lista.append(nmr)
          print(lista)

 