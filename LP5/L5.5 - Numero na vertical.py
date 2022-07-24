'''
Entrada
    O programa recebe dois números inteiros N≥0 (o número a ser representado 
    no formato vertical) e V≥0 (o número de vezes).
Saída
    O programa deve imprimir V vezes o número N, como especificado nos exemplos. 
    Note que após o último número na vertical (i.e., última coluna) não deve haver
    espaçamento.
'''
n = input()
v = int(input())

def number_digits(n: int = None):
    '''
    Args:
        n (int): It's a integer.
    Returns:
        number_digits (int): This represents the number of digits in a number n.
    '''

    number_digits = 1

    while n >= 10 ** number_digits - 1:
        number_digits += 1

    return number_digits

for digit in n:
    s = f'{digit} ' * v
    print(s.strip())
