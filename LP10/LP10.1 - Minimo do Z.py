'''
Entrada
    A primeira linha da entrada tem um número positivo N, representando, o número de linhas e colunas da matriz quadrada. 
    Cada uma das próximas N linhas tem N inteiros (positivos ou negativos), que descrevem os valores lidos em cada célula da matriz.
Saída
    A saída é uma única linha com um inteiro, indicando o valor mínimo encontrado nos elementos da matriz na forma Z.
'''

class Matrix:
    def __init__(self, matrix) -> None:
        self.matrix : list[list[int]] = matrix
        self.shape: tuple = (len(matrix), len(matrix[0]))
    
    def min_z(self) -> int:
        """_summary_

        Returns:
            min_z (int): It's mininum value in matrix shape z 
        """

        z_list: list[int] = list()

        for i, row in enumerate(self.matrix):
            if i == 0 or i == len(self.matrix) - 1:
                z_list.extend(row)
            else:
                z_list.append(self.matrix[i][-i-1])

        return min(z_list)

n = int(input())
matrix: list[list[int]] = list()

for i in range(n):
    array = list(map(int, input().split()))
    matrix.append(array)

matrix_obj = Matrix(matrix.copy())
print(matrix_obj.min_z())