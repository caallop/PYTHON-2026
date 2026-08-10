#exercicio 3

soma = 0

for n151 in range (0, 52):
    if n151 %2 != 0:
        print(f"o numero {n151} é impar.")
    else:
        continue
    soma += n151

media = soma/26

print (media)