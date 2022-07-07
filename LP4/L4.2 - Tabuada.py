'''
Entrada
    O seu programa receberá um inteiro positivo N e um inteiro positivo M.
Saída
    O seu programa deve imprimir a tabela de multiplicação do 
    número N, começando de 0 e terminando em M
'''

v = [int(input()) for i in range(2)]

def multiplication_table_print(array_list: list):
    '''
    '''
    n, m = array_list

    for i in range(m + 1):
        print(f"{n} x {i} = {n*i}")

multiplication_table_print(array_list= v)