class Aluno:
    def __init__(self, nome, faculdade, curso, semestre):
        self.nome = nome
        self.faculdade = faculdade
        self.curso = curso
        self.semestre = semestre

    def apresentar(self):

        return f"Ola! sou {self.nome}, estudo na {self.faculdade}, fazendo {self.curso} a {self.semestre} semestres"


# testando objeto
aluno1 = Aluno(
    input("nome: "), input("faculdade: "), input("curso: "), input("semestre: ")
)

print(aluno1.apresentar())

print(aluno1.__dict__)
