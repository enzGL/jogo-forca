from os import system
import random

system('cls')


def imprimirPlvra (palavra, letrasCorretas):
    print(palavra)
    for letra in palavra:
        if letra in letrasCorretas:
         print(letra, end=' ')
        else:
            print('_', end=' ')
    print()


def sorteiaPlvrs(listPlvrs):
    qntdPlvrs = len(listPlvrs) -1
    numAleatorio = random.randint(0, qntdPlvrs)
    return listPlvrs[numAleatorio]

def testeTentativa(palavra, letra, letrasCorretas):
    if letra in palavra:
        letrasCorretas.append(letra)
        print("Letra correta!")
    else:
        print('Letra errada!')

def jogar(lista):
    palavra = sorteiaPlvrs(lista)
    letra = ''
    letrasCorretas = []

    while letra != '0':
        imprimirPlvra(palavra, letrasCorretas)
        letra = input('Digite uma letra: ')
        testeTentativa(palavra, letra, letrasCorretas)

lista = [
    'python', 'php', 'java', 'javascript', 'csharp', 'node', 'html', 'css', 'ruby', 'delphi'
]

jogar(lista)