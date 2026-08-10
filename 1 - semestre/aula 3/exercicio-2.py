#exercicio 2

soma = 0

for n150 in range (0, 51):
    if n150 %2 == 0:
        print(f"o numero {n150} é par.")
    else:
        continue
    soma += n150
print(soma)