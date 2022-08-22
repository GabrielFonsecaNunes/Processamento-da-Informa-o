'''
Entrada
    A entrada é um número floateiro n estritamente positivo, seguidos dos elementos da matriz. Note também que os elementos
    da matriz são lidos no formato tradicional de matriz, isto é, são lidos linha a linha, com um espaço entre dois elementos
    da mesma linha.
Saída
    Seu programa deve imprimir na tela o resultado usando duas casas decimais. Veja nos exemplos abaixo que na saída há o
    texto “Resultado = ” precedendo o valor do resultado propriamente.
'''

class Matrix:
    def __init__(self, matrix) -> None:
        self.matrix : list[list[float]] = matrix
        self.shape: tuple = (len(matrix), len(matrix[0]))
    
    def sum_diagonal(self) -> float:
        """
        Returns:
            sum_diagonal (float): This function get sumarize the elements
            in diagonal matrix
        """
        n, m = self.shape
        list_diagonal: list[float] = list()

        for i in range(n):
            list_diagonal.append(self.matrix[i][i])
        
        return sum(list_diagonal)

    def sum_upper_triangular(self) -> float:
        n, m = self.shape
        list_upper_triangular: list[float] = list()

        for i in range(n):
            for j in range(m):
                element = self.matrix[i][j]
                if i < j:
                    list_upper_triangular.append(element)

        return sum(list_upper_triangular)
        

    def sum_lower_triangular(self) -> float:
        n, m = self.shape
        list_lower_triangular: list[float] = list()

        for i in range(n):
            for j in range(m):
                element = self.matrix[i][j]
                if i > j:
                    list_lower_triangular.append(element)

        return sum(list_lower_triangular)


n = int(input())
matrix: list[list[float]] = list()

for i in range(n):
    array = list(map(float, input().split()))
    matrix.append(array)

matrix_obj = Matrix(matrix.copy())
result = matrix_obj.sum_upper_triangular() + matrix_obj.sum_lower_triangular() - matrix_obj.sum_diagonal()
print("Resultado {result:.2f}".format(result = result))