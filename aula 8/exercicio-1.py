#match/case e while:

#comando sair = -saindo da entrutura.
#case = sair - encerrando
#case qualquer outra coisa - comando invalido

while True:
    comando = input("Digite sair parar: ")

    match comando:
        case 'sair':
            print('encerrando!')
        case _:
            print("comando invalido!!!!!!")
