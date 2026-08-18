class Lucro:
    def __init__(self, nome, capital, taxa, tempo):
        self.nome = nome
        self.capital = capital
        self.taxa = taxa
        self.tempo = tempo

    def calculo(self):
        montante = self.capital * (1 + self.taxa / 100) ** self.tempo
        lucro = montante - self.capital
        return lucro

r1 = Lucro("luiz", 100000000, 5, 1000)
r2 = Lucro("valeria", 10, 8, 1000)
r3 = Lucro("eu", 10, 500, 10)
print(f"o(a) {r1.nome} ganhou:{r1.calculo()}")
print(f"o(a) {r2.nome} ganhou:{r2.calculo()}")
print(f"o(a) {r3.nome} ganhou: {r3.calculo()}")

# for i in range(3):
#     print(i)
