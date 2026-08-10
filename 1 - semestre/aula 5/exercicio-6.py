#Exercício 6: entre a soma dos numeros em uma lista usando while 
lista = [23, 45, 12, 10, 25]
i = 0
soma = 0 
while i < len(lista):
    soma += lista[i]
    i += 1
    print(i)
    
print(soma)