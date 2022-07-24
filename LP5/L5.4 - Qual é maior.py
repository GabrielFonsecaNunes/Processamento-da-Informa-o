'''
Entrada
    Seu programa receberá 3 números: Float inicial para a equação 2x Float inicial para a equação x**2
    Quantidade de iterações

Saída
    Ao fim das iterações, seu programa deve imprimir 0 caso a equação 2x produziu o maior número ou 1 caso a equação x2 produziu o maior número. Em caso de empate, seu programa deve imprimir 0.
'''

array_list = [float(input()) for i in range(3)]

def bigger(array_list: list = None):
    '''
    Args:
        array_list (list): It's a list with 
    Return:
    '''
    n = array_list[0]
    m = array_list[1]
    k = array_list[2]
    a = [n]
    b = [m]

    for i in range(int(k)):
        a.append(2*a[-1]) 
        b.append(b[-1]**2)

    return 0 if a[-1] > b[-1] else 1

print(bigger(array_list= array_list))