nome = str(input("qual o nome de usuario?"))
sobrenome = str(input("qual o sobrenome de usuario?"))
cpf = str(input("qual o cpf de usuario?"))

nomecerto = "juan"
sobrenomecerto = "makita"
cpfcerto = "12312312345"

if nome == nomecerto and sobrenome == sobrenomecerto and cpf == cpfcerto:
    print("acesso vip concedido!")
elif nome == nomecerto or sobrenome == sobrenomecerto and cpf == cpfcerto:
    print("analise para acesso em andamento")
else:
    print("acesso negado!")