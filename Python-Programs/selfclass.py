class Pessoa:
    def __init__(self, nome, idade,altura,signo):
        self.nome=nome
        self.idade=idade
        self.altura=altura
        self.signo=signo
pessoa=Pessoa('Cláudio',33,'1,77cm','Escorpião')
print(pessoa.nome)
print(pessoa.idade)
print(pessoa.altura)
print(pessoa.signo)
