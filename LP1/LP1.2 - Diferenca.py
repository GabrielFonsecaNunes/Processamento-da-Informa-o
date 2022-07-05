'''
Leia quatro números inteiros A, B, C e D. A seguir, calcule e mostre a 
diferença do produto de A e B pelo produto de C e D segundo a fórmula: 
DIFERENCA = (A * B - C * D).
Entrada:
    A entrada contém quatro números inteiros.
Saída:
    Seu programa deve imprimir na tela a mensagem DIFERENCA com todas as 
    letras maiúsculas, conforme exemplo abaixo, com um espaço em branco 
    antes e depois da igualdade.
'''

v = []

for i in range(4):
    v.append(int(input()))

def different(vector: list = None):
    '''
    Args:
        vector (list): It's intergers list
    Return:
        dif (int): dif = (vector[0] * vector[1] - vector[2] * vector[3]).
    '''
    dif = (vector[0] * vector[1] - vector[2] * vector[3])

    print(f"DIFERENCA = {dif}")

different(vector = v)