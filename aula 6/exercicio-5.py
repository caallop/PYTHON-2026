for i in range(3):
    senha = input("Digite sua senha: ")
    if senha == "sair":
        print(senha)
        break


while True:
    nome = input("Digite seu nome: ")
    if nome == "sair":
        break
    print(nome)