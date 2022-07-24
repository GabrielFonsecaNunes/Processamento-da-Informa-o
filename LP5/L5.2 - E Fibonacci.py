'''
Entrada
    O programa recebe um número inteiro maior ou igual a zero.
Saída
    O programa deve imprimir “Verdadeiro” (sem aspas) se o número dado como 
    entrada pertence à sequência de Fibonacci, caso contrário deve imprimir 
    “Falso” (sem aspas).
'''
n = int(input())

def fib_series(n: int, lst=None):
    '''
    Args:
        n (int): The number of element in fibonnaci series
    Returns:
        number_fib (int): The fibonnaci series
    '''
    if lst is None:
        lst = [0, 1]
    while len(lst) < n:
        lst.append(lst[-2] + lst[-1])
    return lst

fib_list = fib_series(n = 70)

print("Verdadeiro" if n in fib_list else "Falso")