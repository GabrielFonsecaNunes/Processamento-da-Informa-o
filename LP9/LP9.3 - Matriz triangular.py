'''
Entrada
    A primeira linha da entrada contém o número de linhas da matriz 
    (o número de colunas é igual ao de linhas, já que a matriz é quadrada). 
    As demais linhas da entrada representam os elementos contidos nas linhas
    da matriz. Por exemplo, a matriz A é representada na entrada da seguinte forma:

    Os elementos da matriz podem ser qualquer número real.

    3
    1 2 3
    0 8 1
    0 0 1

Saída
    A saída deve dizer se a matriz fornecida é: nao triangular, triangular superior, triangular inferior ou diagonal.
'''

class Matrix:
    def __init__(self, matrix) -> None:
        self.matrix : list[list[float]] = matrix
        self.shape: tuple = (len(matrix), len(matrix[0]))

    
    def transpose(self):
        """
        Returns:
            matrix_transpose (list[list[int]]): This function transpose 
            the matrix.
        """
        n, m = self.shape
        matrix_transpose :list[list[int]] = list()

        for i in range(n):
            for j in range(m):
                matrix_transpose[i][j] = self.matrix[j][i]

        return matrix_transpose

    def is_diagonal(self) -> bool:
        """
        Returns:
            bool: This function check if matrix is 
            diagonal
        """
        n, m = self.shape
        for i in range(n):
            for j in range(m):
                if i != j and self.matrix[i][j] != 0:
                    return False
        return True

    def is_upper_triangular(self) -> bool:
        """
        Returns:
            bool: This function check if matrix is 
            upper triangular
        """
        n, m = self.shape
        if self.is_diagonal() == False:
            for i in range(n):
                for j in range(m):
                    element = self.matrix[i][j]
                    if i > j and element != 0:
                        return False
            return True
        else:
            return False

    def is_lower_triangular(self) -> bool:
        """
        Returns:
            bool: This function check if matrix is 
            lower triangular
        """
        n, m = self.shape
        if self.is_diagonal() == False:
            for i in range(n):
                for j in range(m):
                    element = self.matrix[i][j]
                    if i < j and element != 0:
                        return False
            return True
        else:
            return False


n = int(input())
matrix: list[list[float]] = list()

for i in range(n):
    array = list(map(float, input().split()))
    matrix.append(array)

obj = Matrix(matrix.copy())

if obj.is_upper_triangular():
    print("triangular superior")

elif obj.is_lower_triangular():
    print("triangular inferior")

elif obj.is_diagonal():
    print("diagonal")
else:
    print("nao triangular")