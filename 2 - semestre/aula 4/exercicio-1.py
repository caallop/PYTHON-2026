# Ex.58 - Crie um algoritmo para calcular o desconto e mostrar o respectivo salário de uma determinada pessoa.

# Insira nome, salario, taxa de desconto (27,5%) e retorne o valor de desconto e o valor a ser recebido.

# Faça o teste para duas ou três pessoas. 

class Salario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def calculoDeDesconto(self):
        return f"{self.nome}, o valor que você irá receber é de {self.salario * 0.725}, pois você terá um desconto de {self.salario * 0.275}."

s1 = Salario(('Sabrina'), (10000))
s2 = Salario(('Lucas'), (600))
s3 = Salario(('Rafael'), (1600))

print(s1.calculoDeDesconto())
print(s2.calculoDeDesconto())
print(s3.calculoDeDesconto())