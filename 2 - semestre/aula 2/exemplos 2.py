cliente = {}
#cliente ['nome'] = input("digite o nome ")
#cliente ['idade'] = input("digite a idade ")

print(cliente)


cliente = {
    'nome': ['vitoria'],
    'idade': ['30'],
}
print(f"----------------------------------------------\n {cliente}")
cliente['idade'] = 31
print(f"----------------------------------------------\n {cliente}")
cliente.update({'tel': 11997764440})
print(f"----------------------------------------------\n {cliente}")
del cliente['nome']
print(f"----------------------------------------------\n {cliente}")
tel = cliente.pop("tel")
print(f"----------------------------------------------\n {cliente}")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
produto = {'preco': int(input("Qual o valor: ")), 'estoque': 3}

if produto['preco'] >= 1000:
    categoria = 'Alto valor'
elif produto['preco'] >= 200:
    categoria = 'Médio valor'
else:
    categoria = "Baixo valor"
    
print(categoria)
print(produto)


# o metodo .items() devolve os elementos do dicionario em formato de pares