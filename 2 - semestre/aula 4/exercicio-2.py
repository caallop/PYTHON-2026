# 2 - Para o exercício anterior, crie mais 4 objetos, crie uma lista de objetos, depois utilize uma estrutura de repetição para mostrar um texto com o respectivo desconto e salário a receber para cada pessoa.

class Salario:
    def __init__(self, nome, salario, desconto):
        self.nome = nome
        self.salario = salario
        self.desconto = desconto
    def salarioAReceber(self):
        return self.salario * self.desconto
    def descontoTotal(self):
        return self.desconto

p1 = Salario('Rafael', 1600, 0.275)
p2 = Salario('Rafael', 1600, 0.275)
p3 = Salario('Rafael', 1600, 0.275)
p4 = Salario('Rafael', 1600, 0.275)
p5 = Salario('Rafael', 1600, 0.275)

lista_de_salarios = [p1, p2, p3, p4, p5]

for i in lista_de_salarios:
    print(i.salario_receber)
    print(i.descontoTotal)
