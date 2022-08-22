'''
Entrada:
    A primeira linha da entrada contém um inteiro N, representando a dimensão do 
    tabuleiro. Cada uma das N linhas seguintes contém N inteiros positivos Xi, 
    definindo os números em cada posição do tabuleiro.

Saída:
    Seu programa deve produzir uma única linha, contendo um único inteiro, o peso
    máximo entre todas as posições do tabuleiro.

    6
    4 1 3 8 4 5
    9 2 8 9 2 7
    5 5 4 3 2 5
    8 2 9 1 9 8
    7 1 3 2 1 2
    5 1 2 9 3 8
'''

class Matrix:
    def __init__(self, matrix) -> None:
        self.matrix : list[list[int]] = matrix
        self.shape: tuple = (len(matrix), len(matrix[0]))
   
    def find_sum_max_tower(self):
        n, m = self.shape

        tower_max = 0        
        array: list[int] = list()

        for i in range(m):
            for j in range(n):
                element = self.matrix[i][j]

                row_without_element : list[int] = self.matrix[i].copy()
                row_without_element.remove(element)

                col_without_element : list[int] = list()

                for k in range(m):
                    if k != i:
                        col_without_element.append(self.matrix[k][j])

                array = row_without_element + col_without_element
            
                tower_max = max(tower_max, sum(array))

        return tower_max


n = int(input())
matrix: list[list[int]] = list()

for i in range(n):
    array = list(map(int, input().split()))
    matrix.append(array)

chessboard = Matrix(matrix)
print(chessboard.find_sum_max_tower())