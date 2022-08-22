'''
Entrada
    Você receberá dois números inteiros positivos em uma linha indicando a quantidade de
    linhas e de colunas da matriz. Depois, receberá uma matriz, uma linha por linha, com
    o tamanho informado. Por fim, receberá os números, um por linha, visitados aleatoriamente
    dessa matriz. A quantidade de números visitados é sempre igual à quantidade de números da
    matriz, ou seja, a quantidade de números visitados a serem lidos é igual à quantidade de
    linhas vezes a quantidade de colunas.
Saída
    Responda “yes” caso todos os números tenham sido visitados; “no” caso contrário.    
'''
def replace_values(items: list() = None, element = None) -> list():
        """
        Args:
            element (Any): Element to replace
            items (list): It's list any elements
        Returns:
            items: It's the list of items already replace value
        """
        items = [True if element == item else item for item in items]
        return items


class Matrix:
    def __init__(self, matrix) -> None:
        self.matrix : list[list[int]] = matrix
        self.shape: tuple = (len(matrix), len(matrix[0]))
    
    def check_visit(self, elements):
        """
        This function checks if all numbers in the matrix
        have been visited
        Args:
            elements (list[int]): Elements to check.

        Returns:
            flag (str): If all numbers in matrix have 
            benn visited return "yes" else "no" 
        """
        evaluate_matrix = self.matrix.copy()

        for element in elements:
            for i, row in enumerate(self.matrix):
                if element in row:
                    evaluate_matrix[i] = replace_values(evaluate_matrix[i], element)

        for row in evaluate_matrix:
            for element in row:
                if element != True:
                    return "no"
        return "yes"

matrix: list[list[int]] = list()
n, m = [int(value) for value in input().split()]

for i in range(n):
    array = [int(value) for value in input().split()]
    matrix.append(array)

obj = Matrix(matrix)
elements = [int(input()) for i in range(n*m)]

print(obj.check_visit(elements))