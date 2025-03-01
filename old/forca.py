from os import system
import random

system('cls')

#def -> declaração de uma função
#nome da função
#(nomevariavel) -> as variaveis que usaremos em nossa função
#(nomevariavel:str) -> declarando o tipo da varivel
#(nomevariavel = '') -> declarando um valor padrão para caso o usuario não preencha
#() -> str:-> declarando o tipo de retorno

def imprimirPlvra (palavra:str = '', letrasCorretas:list[str] = []):
    # print(palavra)
    for letra in palavra:
        if letra in letrasCorretas:
         print(letra, end=' ')
        else:
            print('_', end=' ')
    print()


def sorteiaPlvrs(listPlvrs: list[str]) -> str:
    qntdPlvrs = len(listPlvrs) -1
    numAleatorio = random.randint(0, qntdPlvrs)
    return listPlvrs[numAleatorio]

def testeTentativa(palavra: list[str], letra:str, letrasCorretas:list[str]) -> bool:
    system('cls')
    if letra in palavra:
        letrasCorretas.append(letra)
        return True
    else:
        return False


def jogar(lista:list[str]):
    palavra = sorteiaPlvrs(lista)
    letra = ''
    letrasCorretas = []

    while letra != '0':
        imprimirPlvra(palavra, letrasCorretas)
        letra = input('Digite uma letra: ')

        if letra in letrasCorretas:
            system('cls')
            print('Você já tentou essa letra...')
            continue

        if  testeTentativa(palavra, letra, letrasCorretas,):
            print('Acertou !')

        todasLetrasCorretas = True

        for letra in palavra:
            if letra not in letrasCorretas:
                todasLetrasCorretas = False

        if todasLetrasCorretas:
            system('cls')
            print('Você acertou a palavra!')
            print(f'A palavra era {palavra}')
            break

lista = [
    'python', 'php', 'java', 'javascript', 'csharp', 'node', 'html', 'css', 'ruby', 'delphi'
]

jogar(lista)