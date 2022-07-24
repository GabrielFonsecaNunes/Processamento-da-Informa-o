'''
Faça um programa que receba uma lista de números natural e contabilize 
quantos desses números são primos. Lembre-se, um número x é primo se 
x > 1 e seus únicos divisores são 1 e o próprio x.

Entrada
    O seu programa irá receber um número inteiro N. Seguidamente, uma sequência de N números naturais, um por linha.
Saída
    O programa gera apenas uma linha de saída no formato “dos <N> numeros informados <P> eram primos”, com todas as letras minúsculas e sem acentos, onde <N> deve ser substituído pelo valor de N e <P> pela quantidade de números primos dentro os N números fornecidos. 
'''

def is_cousin_prime(n: int = None) -> bool:
    '''
    Args:
        n (int): It's a number which we want to check
    Returns:
        flag (bool): If number is cousin prime
    '''
    if n % 2 == 0 and n != 2 or n == 1:
        return False

    for i in range(2, n):
        if n % i == 0 and i != n:
            return False
    return True

def count_cousin_prime(array_list: list = None):
    '''
    Args:
        array_list (list): It's a list intergers
    Returns:
        sum (int): It's a count cousion prime in list 
    '''
    sum = 0
    for number in array_list:
        if is_cousin_prime(n = number):
            sum += 1
    return sum

l = int(input())
v = [int(input()) for i in range(l)]

print(f"dos {l} numeros informados {count_cousin_prime(array_list = v)} eram primos")