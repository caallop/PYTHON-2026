#exercício 11 - crie uma matriz 3x3

lista = []

for i in range (3):
  nmr1 = str(input("digite o o numero 1 da fileira {i} "))
  nmr2 = str(input("digite o o numero 2 da fileira {i} "))
  nmr3 = str(input("digite o o numero 3 da fileira {i} "))
  numbers = [nmr1, nmr2, nmr3]
  lista.append(numbers)

print(lista[0])
print(lista[1])
print(lista[2])