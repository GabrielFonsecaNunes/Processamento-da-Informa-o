'''
Entrada
    A entrada é um número inteiro ímpar n, n≥1 , seguidos dos elementos
    da matriz. Note que os elementos da matriz são lidos no formato tradi-
    cional de matriz, isto é, são lidos linha a linha, com um espaço entre
    dois elementos da mesma linha.

Saída
    Seu programa deve imprimir na tela o resultado usando duas casas decimais.
    Veja nos exemplos abaixo que na saída há o texto “Resultado = ” (com um espaço
    no final) precedendo o valor do resultado propriamente.
'''

class Matrix:
    def __init__(self, matrix) -> None:
        self.matrix : list[list[float]] = matrix
        self.shape: tuple = (len(matrix), len(matrix[0]))

    def sum_tup_cup(self):
        """
        Returns:
            s (float): It's a sum the top cup 
            in matrix
        """
        n, m = self.shape
        i = 0
        s = 0
        if m > 1:
            while (m-i) // 2 >= 1:
                s += sum(self.matrix[i][i:m-i])
                i += 1
        else:
            s += self.matrix[0][0]

        return f"Resultado = {s:.2f}"

n = int(input())
matrix: list[list[float]] = list()

for i in range(n):
    array = list(map(float, input().split()))
    matrix.append(array)

matrix_obj = Matrix(matrix.copy())
print(matrix_obj.sum_tup_cup())