from Veiculos import Veiculos

class Moto(Veiculos):
    def __init__(self, modelo, marca):
        super().__init__(modelo, tipo="Moto")
        self._marca = marca

    def acelerar(self):
        print(f'{self._modelo} esta acelerando até 140Km/h')