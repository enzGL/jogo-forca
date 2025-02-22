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

def testeTentativa(palavra, letra, letrasCorretas, letrasTentadas):
    system('cls')
    if letra in palavra:
        letrasCorretas.append(letra)
        return True
    else:
        return False

def jogar(lista):
    palavra = sorteiaPlvrs(lista)
    letra = ''
    letrasCorretas = []
    letrasTentadas = []

    while letra != '0':
        imprimirPlvra(palavra, letrasCorretas)
        letra = input('Digite uma letra: ')

        if letra in letrasCorretas:
            system('cls')
            print('Você já tentou essa letra...')
            continue

        if  testeTentativa(palavra, letra, letrasCorretas, letrasTentadas):
            print('Acertou !')
        else: 
            if letra in letrasTentadas:
                print('Errou !')
            else:
                print(f"{letrasTentadas}", end='-')
                print('Errou !')

lista = [
    'python', 'php', 'java', 'javascript', 'csharp', 'node', 'html', 'css', 'ruby', 'delphi'
]

jogar(lista)