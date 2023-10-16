from Cachorro import Cachorro
from Gato import Gato

c1 = Cachorro("Claudio", "Caramelo")
g1 = Gato("Sata", "Cinza")

c1.emitirSom()
g1.emitirSom()

c1.buscar()
g1.arranhar()

c1.brincar('dono', 'bolinha')
g1.brincar('corda')