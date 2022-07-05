'''
Faça um programa que leia dois números inteiros e apresente o maior dos 
dois valores. Nesta questão está proibido usar if (isto é, não deve se 
usar nenhuma estrutura condicional) ou a função max.
Dica: A seguinte fórmula permite calcular apenas o maior valor dados os 
números x e y:

Entrada
    A entrada contém dois números inteiros.
Saída
    Seu programa deve imprimir na tela o maior dos dois valores, conforme 
    exemplo fornecido.    
'''

v = []

for i in range(2):
    v.append(float(input()))

def max(vector: list = None):
    '''
    Args:
        vector (list): It's a intergers
    Return:
        max (int): The number max in vector
    '''
    m = int(0.5 * (vector[0] + vector[1]) + 0.5 * abs(vector[1] - vector[0]))
    return m

print(f'O maior inteiro: {max(vector= v)}')