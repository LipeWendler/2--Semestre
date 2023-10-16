from Pessoa import Pessoa #Importa a classe mão

class Professor (Pessoa):
    def __init__(self, nome):
        super().__init__(nome) #Passa o nome para a classe mãe

    def saudar(self):
        return f'Olá, eu sou o professor {self.nome}'