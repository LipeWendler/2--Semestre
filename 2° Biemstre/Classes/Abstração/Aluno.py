from Pessoa import Pessoa #Importa a classe mão

class Aluno(Pessoa):
    def __init__(self, nome):
        super().__init__(nome) #Passa o nome para a classe mãe

    def saudar(self):
        print(f'Olá, eu sou o aluno {self.nome}')