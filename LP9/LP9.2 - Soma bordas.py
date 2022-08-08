'''
Entrada
    A entrada são dois números inteiros (maiores ou iguais a 3), seguidos 
    dos elementos da matriz. Note que nos exemplos abaixo a primeira linha
    é usada para ler esses dois números inteiros (com um espaço entre eles).
    Note também que os elementos da matriz são lidos no formato tradicional 
    de matriz, isto é, são lidos linha a linha, com um espaço entre dois elementos
    da mesma linha.
Saída
    Seu programa deve imprimir na tela o resultado usando duas casas decimais. 
    Veja nos exemplos abaixo que na saída há o texto “Borda = ” precedendo o
    valor da soma propriamente.
'''

n, m = list(map(int, input().split()))

matrix: list[list[float]] = list()

for i in range(n):
    # Matrix.append([float(element) for element in input().split()])
    matrix.append(list(map(float, input().split())))

def bolder_sum(matrix: list[list[float]] = None) -> float:
    """
    Args:
        matrix (list[list[int]], optional): _description_. Defaults to None.

    Returns:
        int: _description_
    """
    soma = 0.0
    for i, array in enumerate(matrix):
        if i == 0 or i == len(matrix) - 1:
            soma += sum(array)
        else:
            soma += array[0] + array[-1]
    return soma

print(f"Borda = {bolder_sum(matrix):.2f}")