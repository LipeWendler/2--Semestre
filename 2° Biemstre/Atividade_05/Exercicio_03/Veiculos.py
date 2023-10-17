'''
Herança de Veículos:
Crie uma classe Veiculo com atributos como 
tipo e velocidade e, em seguida, crie classes 
Carro e Moto que herdem de Veiculo.
'''

class Veiculos:
    def __init__(self, modelo, tipo):
        self._modelo = modelo
        self._tipo = tipo

    def acelerar(self):
        print(f'O {self._modelo} está acelerando!')