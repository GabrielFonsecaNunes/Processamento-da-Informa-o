'''
 Desenvolva um programa com as seguintes funções:

a. uma função que preenche um vetor com N valores reais informados pelo usuário e retorna 
este vetor. A variável N deve ser recebida como parâmetro da função.

b. uma função que recebe um vetor por argumento e verifica se há números com valores repetidos no vetor. 
   A função deve imprimir os valores dos números repetidos (veja os exemplos de entrada e saída).
   Seu programa deve ler o número N, chamar a função do item (a) e em seguida a função do item (b).

Entrada
    Contém um número inteiro N positivo seguido de N valores reais.

Saída
    Impressão do valores dos números reais repetidos (um número em cada linha).
'''

def get_decimal_list(N: int) -> list[float]:
    '''
    Args:
        N (int): It's the amount of numbers we need to 
        add to the arraylist
    Returns:
        decimal_list (list[float]): It's a float list 
    '''
    decimal_list = []
    for i in range(N):
        decimal_list.append(float(input()))
    return decimal_list

def print_repeat_numbers(array: list[float]):
    '''
    Args:
        array (list[float]): It's list of floats
    '''
    v = list[float]
    p = list()

    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] == array[j] and i != j and array[i] not in p:
                p.append(array[i])
    
    for element in p:
        print(element)

n = int(input())
v = get_decimal_list(N= n)
print_repeat_numbers(array= v)