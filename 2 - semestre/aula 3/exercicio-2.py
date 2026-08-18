class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


r1 = Retangulo(float(input("Base: ")), float(input("altura: ")))
print(f"A área do r1: {r1.area()} - perimetro: {r1.perimetro()}")