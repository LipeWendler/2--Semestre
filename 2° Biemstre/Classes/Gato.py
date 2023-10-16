from Animal import Animal

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, especie="Gato")
        self.cor = cor

    def emitirSom(self): #OVERRIDE
        print(f'{self.nome} miou! (miau miau)')
    
    def arranhar(self):
        print(f'{self.nome} arranhou o sofa!')

    def brincar(self, brinquedo): #OVERLOAD
        print(f'{self.nome} está brincando com o {brinquedo}')