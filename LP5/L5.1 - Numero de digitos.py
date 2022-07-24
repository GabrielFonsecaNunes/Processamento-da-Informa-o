'''
Entrada:
    O programa recebe um número inteiro, N, maior a zero. Está proibido o 
    uso da função comprimento de strings. A entrada deve ser obrigatoriamente 
    um número inteiro e deve usar um laço para resolver a questão.
Saída:
    O programa deve imprimir o número de dígitos de N.
'''

n = int(input())

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

print(number_digits(n = n))