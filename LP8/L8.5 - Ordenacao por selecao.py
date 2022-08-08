'''
Entrada
    A entrada para o seu programa será uma lista de 10 inteiros representando os elementos do vetor que devem ser ordenados.

Saída
    A saída deve conter os índices de todas as trocas feitas pela função do item (b) e ao final, deve exibir o vetor ordenado.
'''

def sort(array):
    for p in range(0, len(array)):
        current_element = array[p]

        while p > 0 and array[p - 1] > current_element:
            
            array[p] = array[p - 1]
            p -= 1
        print(f"TROCA {current_element} {array[p]}")
        array[p] = current_element

    return array

array = [int(input()) for i in range(10)]

print(sort(array= array))