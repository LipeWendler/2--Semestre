from abc import ABC, abstractmethod

class Pessoa (ABC): 
    def __init__(self, nome): #Cria o objeto
        self.nome = nome

    @abstractmethod #Define método abstrata
    def saudar (self):
        pass




