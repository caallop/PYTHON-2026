pessoa = {}
pessoa = {}

pessoa['nome'] = input("qual é o nome do aluno? ")
pessoa['nota_1'] = int( input("qual é nota 1 do aluno? "))
pessoa['nota_2'] = int(input("qual é nota 2 do aluno? "))
pessoa['nota_3'] = int(input("qual é nota 3 do aluno? "))

media = (pessoa['nota_1']+pessoa['nota_2']+pessoa['nota_3'])/3
if media >=6:
    print(f"\naprovado com: {media}")
else:
    print(f"reprovado com: {media}")
