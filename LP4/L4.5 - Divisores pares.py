'''
Entrada
    Um único número inteiro N, tal que 0 ≤ N ≤ 10000.
Saída
    Seu programa deve imprimir uma única linha contendo um número que represente a quantidade de divisores pares de N.
'''

n = int(input())

def count_even_divisors(n: int = None) -> int:
    '''
    Args:
        n (int): It's number
    Return:
        s (int): It's quantity even divisor numbers by n
    '''
    s = 0
    for i in range(2, n+1, 2):
        if n % i == 0:
            s += 1
    return s

print(count_even_divisors(n = n))