# ex. 1

comando = "start"

if comando == "start":
    print("iniciando")
elif comando == "stop":
    print("parando")

else:
    print("entrada invalida!")

# ===========================================================================================================================

# ex 1 - match/case

match comando:
    case "start":
        print("iniciando")
    case "stop":
        print("parando")

    case _:
        print("entrada invalida!")


# ex 2 - match/case

opcao = input("digite um numero")

match comando:
    case "1":
        print("cadastrar")
    case "2":
        print("parando")
    case "3":
        print("")

    case _:
        print("entrada invalida!")

# Exemplo 3 com match/case

dados = ("produtos", "arroz", 10)

match dados :
  case ("produto", nome, qtd):
    print(f"{nome} - {qtd}")
  case _:
    print("Entrada inválida")

numero = int(input("Entre com um número: "))

match numero:
  case _ if (numero %2 == 0):
    print("Par!")
  case _:
    print("Impar")