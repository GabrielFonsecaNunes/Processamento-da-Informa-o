'''
Entrada
    O programa recebe dois números inteiros L≥ 1 e C≥1 que representam 
    o número de linhas e número de colunas do retângulo.
Saída
    O programa deve desenhar as bordas do retângulo de dimensão L x C. 
    A parte interna do retângulo deve estar preenchida de espaços em branco.
'''

v = [int(input()) for i in range(2)]

def print_show_bolder(array: list = None):
    '''
    Args:
        array (list): It's a array with 2 numbers
    Return:
        figure (str): It's a figure
    '''
    n, m = array
    
    if n == 1:
        print("*" * m)
    
    else:
        for i in range(n):
            if i == 0 or i == n - 1 or m == 1:
                print("*" * m)
            else:
                e = " " * (m - 2)
                print(f"*{e}*")

print_show_bolder(array= v)