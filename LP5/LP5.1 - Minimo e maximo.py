'''
Entrada
    O programa recebe um número inteiro N≥1 que representa a quantidade de elementos a serem lidos. Seguidamente, uma sequência de N números inteiros é apresentada. Os números inteiros, na sequência, estão no intervalo [-1000000,1000000].
Saída
    O programa deve imprimir o valor máximo e o valor mínimo, segundo exemplos apresentados abaixo. As palavras devem ir sem acentos.
    Obs. Não deve utilizar a estrutura de listas ou vetores. Caso identificado o uso de Listas/Vetores na sua solução a nota será zero.
'''
def max(vector: list = None):
    '''
    Args:
        vector (list): It's a intergers
    Return:
        max (int): The number max in vector
    '''
    m = int(0.5 * (vector[0] + vector[1]) + 0.5 * abs(vector[1] - vector[0]))
    return m

def min(vector: list = None):
    '''
    Args:
        vector (list): It's a intergers
    Return:
        min (int): The number min in vector
    '''
    m = int(0.5 * (vector[0] + vector[1]) - 0.5 * abs(vector[1] - vector[0]))
    return m
    
n = int(input())

max_value = int(input())
min_value = max_value

for i in range(n - 1):
    value = int(input())
    max_value = max(vector= [max_value, value])
    min_value = min(vector= [min_value, value])

print(f"minimo = {min_value}")
print(f"maximo = {max_value}")