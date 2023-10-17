'''
Herança de Veículos:
Crie uma classe Veiculo com atributos como 
tipo e velocidade e, em seguida, crie classes 
Carro e Moto que herdem de Veiculo.
'''

'''
Sobrescrevendo Métodos:
Na classe Veiculo, crie um método chamado descricao() 
que imprima uma descrição básica do veículo. Sobrescreva 
esse método nas classes Carro e Moto para fornecer descrições 
specíficas para cada tipo de veículo.
'''

'''
Polimorfismo com Métodos:
Crie uma função chamada acelerar(veiculo) que aceita qualquer
objeto Veiculo e aumenta sua velocidade. Teste essa função com 
instâncias de Carro e Moto.
'''


class Veiculos:
    def __init__(self, modelo, tipo, funcionando = False):
        self._modelo = modelo
        self._tipo = tipo
        self._funcionando = funcionando

    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def funcionando(self):
        return self._funcionando
    
    @funcionando.setter
    def funcionando(self, funcionando):
        self._funcionando = funcionando


    def ligar(self):
        print(f'O {self._modelo} está ligado!')

    def descrever(self):
        print(f'Tipo: {self._tipo}')
        print(f'Modelo: {self._modelo}')

    def acelerar(self, velocidade):
        if not self._funcionando:
            print(f'{self.modelo} não está ligado!')

        print(f'{self._modelo} está acelerando a {velocidade}Km/h!')


        