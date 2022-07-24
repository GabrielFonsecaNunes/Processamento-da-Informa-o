'''
Faça um programa que dado dois números naturais determine se eles 
são amigos.
Entrada
    A entrada consiste de dois números inteiros X e Y, dados nesta 
    respectiva ordem.
Saída
    A saída consiste de uma única linha contendo a frase “amigos”, 
    caso X e Y sejam números amigos, e a frase “nao amigos”, caso 
    contrário.
'''

v = [int(input()) for i in range(2)]

def friend_numbers(array_list: list = None):
    '''
    Args:
        array_list (list): It's a list, this list there are only
        two numbers.
    Return:
        flag (bool): It's flag if numbers are friends or aren't.
        A number will be a friend only the sum divisors it's equal
        the other number and diffent from each other.
    '''
    sum_divisors_n = 0
    sum_divisors_m = 0

    n, m = array_list

    for i in range(1, max(n, m) + 1):
        if n % i == 0:
            j += i
        
        if m % i == 0:
            k += i
    
    return "amigos" if sum_divisors_n == sum_divisors_m and m != n else "nao amigos"

print(friend_numbers(array_list= v))

