'''
A fórmula para calcular a área de uma circunferência é: área = pi*raio². Considerando para
este problema que pi é igual a 3.14159. Efetue o cálculo da área, elevando o valor de raio ao
quadrado e multiplicando por pi.

Entrada:
    A entrada contém um número real, positivo, representando o raio.
Saída:
    Seu programa deve imprimir na tela a área do círculo com 4 casas após o ponto decimal.
'''

import math

r = float(input())

def area(radis: float = None):
    '''
    Args:
        radius (float): It's a radius of circle
    Return:
        area (float): It's area of circle
    '''
    PI = math.pi
    return (PI * r ** 2) 

print(f"{area(radis= r):.4f}")