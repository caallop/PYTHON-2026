# exercício 8 - crie um algorimo apra simular um sistema de compras, onde deverá ser solicitado nome 100x. após isso crie uma estrutura para solicitar preço, com isso, deixe o respectio nome e preço juntos. finalmente, mostre o valor total do produto
lista = []
preco_final = 0
for i in range(100):
    nome = str(input("qual nome do poduto? (se deseja finalizaar, digite ('n')) "))
    if nome == "n":
        break

    preco = float(input("qual o preço desse produto? "))
    preco_final += preco
    nome_preco = [nome, preco]
    lista.append(nome_preco)

print(f"a lista no final ficou: {lista} ")
print(f"o preço final dos produtos é: {preco_final} ")
