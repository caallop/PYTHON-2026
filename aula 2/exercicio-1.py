userName = str(input("qual o usuario que deseja fazer login?? "))

if userName == "admin":
    passsword = str(input("qual a senha de admin? "))
    
    if passsword == "1234":
        print("acesso total concedido")
    else:
        print("senha de administrador incorreta")
elif userName == "usuario":
    passsword = str(input("qual a senha de usuario?"))
    if passsword == "1234":
        print("bem vindo!")
    else:
        print("senha incorreta.")
else:
    print("usuario não encontrado")