menu = {
    '1': 'Cadastrar' ,
    '2': 'Consultar' ,
    '3': 'Sair'
}

opcao = input('Escolha 1, 2 ou 3: ')
while opcao not in menu:
    opcao = input('opção invalida: ')

print(f'Você escolheu: {menu[opcao]}')


