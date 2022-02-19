import os
from re import sub

def somar(numero1, numero2):
    return numero1 + numero2

def subtrair(numero1, numero2):
    return numero1 - numero2

if __name__ == '__main__':
    resultado = somar(2, 3)
    print(f'Resultado: {resultado}')

    resultado = subtrair(7, 4)
    print(f'Resultado: {resultado}')