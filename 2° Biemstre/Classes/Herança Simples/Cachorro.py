from Animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, raca): #Método construtor
        super().__init__(nome, especie="Cachorro")
        self.raca = raca

    def emitirSom(self): #OVERRIDE
        print(f'{self.nome} late! (roof roof)')

    def buscar(self):
        print(f'{self.nome} busca o pneu!')

    def brincar(self, pesoa, brinquedo): #OVERLOAD
        print(f'{self.nome} está brincando de {brinquedo} com {pesoa}')