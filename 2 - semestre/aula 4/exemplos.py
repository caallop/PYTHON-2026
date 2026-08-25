class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):

        return f"Ola! sou {self.nome}, tenho {self.idade} anos!"


#testando objeto
p1 = Pessoa("luiz",10000)
p2 = Pessoa("guilherme",111)

print(p1.apresentar())
print(p2.apresentar())