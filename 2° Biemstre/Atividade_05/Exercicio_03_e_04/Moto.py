from Veiculos import Veiculos

class Moto(Veiculos):
    def __init__(self, modelo, marca):
        super().__init__(modelo, tipo="Moto")
        self._marca = marca

    def ligar(self):
        print(f'{self._modelo} esta ligado!')

    def Descrever(self):
        print(f'Tipo: {self._tipo}')
        print(f'Modelo: {self._modelo}')
        print(f'Marca: {self._marca}')