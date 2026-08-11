# Usando .get(), verifique se um dicionário cliente tem a chave desconto, se não tiver, aplique 10% por padrão.

cliente = {
    'nome': input('Digite o nome do clinte: '),
    'idade': int(input('Digite a idade do clinte: ')),
    'email': input('Digite o email do clinte: ')
}

if cliente.get('desconto', 'não informado') is 'não informado':
    print('Você tem 10% de desconto!')
else:
    print('Você tem 20% de desconto')