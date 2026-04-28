#Exercício 11: filtrar palavras com letras proibidas, se aparecer palavras com x, não mostrar
lista = []
while True:
    print("(digite sair para sair)")
    palavra = input("digite uma palvra que não contenha x: ")
    if "x" in palavra:
       print("tem x")
    elif palavra == "sair":
        break 
    else:
        lista.append(palavra)
        print(lista)

print(lista)