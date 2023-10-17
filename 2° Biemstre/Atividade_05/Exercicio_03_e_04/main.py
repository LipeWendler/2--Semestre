from Carro import Carro
from Moto import Moto

Mazda = Carro("RX7", 2002)
Motoca = Moto("MT07", "Yamaha")

Mazda.ligar()
Motoca.ligar()

print(40*"=")
Mazda.descrever()
print(40*"-")
Motoca.descrever()
print(40*"=")

#Mazda.acelerar(100)