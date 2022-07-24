'''
Entrada
    A primeira linha contém um número inteiro N (1 < N ≤ 100) representando a quantidade de medições de velocidade
    do motor em um determinado teste. Cada uma das próximas N linhas consiste de um único inteiro M (0 ≤ M ≤ 10000) 
    representando o número de RPM (rotações por minuto) daquela medida.
Saída
    A saída é o índice da medição em que ocorreu a primeira queda de velocidade. Caso não aconteça nenhuma queda, 
    o seu programa de imprimir o número 0.
'''
n = int(input())

values = [int(input()) for i in range(n)]

def check_engine(array_list: list = None):
    '''
    Args:
        array_list (list): It's 
    Returns:
        n (int): It's
    '''
    start_speed = array_list[0]

    for i in range(1, len(array_list)):
        end_speed = array_list[i]
        if end_speed < start_speed:
            return i + 1
        else:
            start_speed = end_speed
    return 0

print(check_engine(array_list= values))