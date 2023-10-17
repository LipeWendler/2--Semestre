from Veiculos import Veiculos

class Carro(Veiculos):
    def __init__(self, modelo, ano):
        super().__init__(modelo, tipo="Carro")
        self._ano = ano

    def ligar(self):
        print(f'{self._modelo} esta Ligado')

    def Descrever(self):
        print(f'Tipo: {self._tipo}')
        print(f'Modelo: {self._modelo}')
        print(f'Ano: {self._ano}')