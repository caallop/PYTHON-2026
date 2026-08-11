livro = {}


livro['total_paginas'] = input("quantas paginas tem o livro?")
livro['paginas_lidas'] = int( input("qual é o saldo? "))

conta = (livro['total_paginas']/livro['paginas_lidas'])*100
print(f"{conta}% ja foi lido")
    