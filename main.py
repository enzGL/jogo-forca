import random
from os import system
from Pessoa import Pessoa

system('cls')

ps = Pessoa('Enzo', 10, 'Sete de Setembro', 323, 'Americana-SP')
ps2 = Pessoa('Paulo', 19, 'Carioba', 99, 'Americana-SP')


# ps.apresentacao()
# ps.apresentaEndereco()

# ps2.apresentacao()
# ps2.apresentaEndereco()

ps.completarFicha(1.70, 'Verde')


print(ps.corOlhos)
print(ps2.corOlhos)