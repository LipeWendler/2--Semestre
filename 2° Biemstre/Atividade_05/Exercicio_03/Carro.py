from Veiculos import Veiculos

class Carro(Veiculos):
    def __init__(self, modelo, ano):
        super().__init__(modelo, tipo="Carro")
        self._ano = ano

    def acelerar(self):
        print(f'{self._modelo} esta acelerando até 200Km/h')
