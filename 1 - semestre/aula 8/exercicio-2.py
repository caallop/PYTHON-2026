#função def

def somar(a,b):
    #o que sera feito com os parametros
    soma = a + b
    sub = a - b
    div = a / b
    mult = a * b
    return soma, sub, div, mult

a, b, c, d = somar(20,10)

print(a)
print(b)
print(c)
print(d)