'''
Entrada
    A primeira linha da entrada consiste de um único número inteiro
    N (N ≥ 1) que indica o número de linhas da matriz de entrada. 
    Os valores contidos na matriz são apresentados nas próximas N 
    linhas da entrada, onde cada linha apresenta os valores contidos
    em uma linha da matriz separados por espaço.
Saída
    A saída do seu programa deve consistir de um único número inteiro
    que representa a soma dos menores valores de cada coluna da matriz.
'''

class Matrix:

    def __init__(self, matrix) -> None:
        self.matrix : list[list[int]] = matrix
        self.shape: tuple = (len(matrix), len(matrix[0]))

    def sum_min_values_col(self) -> int:
        """
        Returns:
           sum_values (int): It's the sum of the minimum values 
           in the columns of the matrix
        """
        # n is number of rows and m numbers of columns
        n, m = self.shape
        # Array mininum values in columns
        values: list[int] = list()
        
        if n == 1 and m == 1:
            return int(self.matrix[0][0])
        elif n == 1 and m > 1:
            return int(sum(self.matrix[0]))
        else:
            for i in range(m):
                try:
                    # Primeiro valor da coluna
                    min_value = self.matrix[0][i]
                    for j in range(n):
                        # Valor para comparacao
                        value = self.matrix[j][i] 
                        if value <= min_value:
                            min_value = value
                    values.append(min_value)
                except IndexError:
                    continue 

        sum_values = int(sum(values))
        return sum_values


n = int(input())
matrix: list[list[float]] = list()

for i in range(n):
    array = list(map(float, input().split()))
    matrix.append(array)

matrix = Matrix(matrix.copy())
print(matrix.sum_min_values_col())