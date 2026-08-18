class Livros:
    def __init__(self, nome, paginas):
        self.nome = nome
        self.paginas = paginas

    def qtdpaginas(self):
        if self.paginas > 300:
            print(
                f"o livro {self.nome} é muito grande!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            )
        else:
            print(
                f"o livro {self.nome} é muito pequeno!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            )


luiz = Livros("luiz", 200)

print(luiz.qtdpaginas())
