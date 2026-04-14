#exercicio 12:crie uma estrutura que solicite itens de compra de forma que só seja possivel sair da estrutura de repetição caso o usuario digite sair. coloque os itens em uma lista

lista = []
resposta = ""
while resposta != "sair":
    print("=================================================")
    print("qual item deseja comprar?")
    print("banana")
    print("maça")
    print("abacate")
    print("se deseja sair, escreva: sair")
    resposta = input("")
    if resposta != "banana" or resposta != "maça" or resposta != "abacate":
        lista.append(resposta)
    elif resposta == "sair":
        continue
    else:
        print("opção invalida")
print(lista)
