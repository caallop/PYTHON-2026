conta_corrente = {}


conta_corrente['nome'] = input("qual é o nome do cliente? ")
conta_corrente['saldo'] = int( input("qual é o saldo? "))
sacar = int( input("quanto quer sacar? "))

if conta_corrente["saldo"] < sacar:
    print (f"saldo insuficiente, esta faltando: {conta_corrente["saldo"] - sacar}$")
else:
    print (f"foi sacado: {sacar}$, sobrou: {conta_corrente["saldo"] - sacar}$")
    