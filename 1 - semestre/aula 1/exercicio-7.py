nome = str(input("qual seu nome? "))
sobrenome = str(input("qual seu sobrenome? "))
cpf = input("qual seu cpf? ")
endereco = str(input("qual seu endereço? "))
cep = int(input("qual seu CEP? "))

nomeCompleto =nome + " " + sobrenome

print(f"nome completo:{nomeCompleto}")
print(f"nome completo e cpf:{nomeCompleto} e {cpf}")
print(f"nome cpf e endereço:{cpf} e {endereco}")