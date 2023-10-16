#HERANÇA
class Animal:
    def __init__(self, nome, especie): #Método construtor
        self.nome = nome
        self.especie = especie
    
    def emitirSom (self): #Atributo da classe
        print(f'{self.nome} faz o URRO!')