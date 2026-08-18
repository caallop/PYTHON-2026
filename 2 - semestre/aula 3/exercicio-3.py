p = 0

class Pessoa:
    def __init__(self, nome, altura, peso):
        self.nome = nome
        self.altura = altura
        self.peso = peso

    def calculo(self):
        return self.peso / (self.altura**2)

    def mostar(self):
        return f"a massa corporal do {self.nome} é: {self.calculo()}"


while p <= 2:
    p += 1
    objeto = Pessoa(input("Nome: "), float(input("altura(M): ")), float(input("peso: ")))
    print(objeto.mostar())
