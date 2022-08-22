'''
Entrada
    A primeira linha da entrada consiste de dois inteiros L e C (1 ≤ L, C ≤ 106) que indicam, 
    respectivamente, o número de linhas e colunas do campo. As próximas L linhas contém exatamente
    C caracteres cada e descrevem o campo minado. Um ladrilho vazio é representado pelo caractere 
    ‘.’ e um com uma mina, por um caractere ‘*’.
Saída
    O seu programa deve imprimir o campo trocando o caractere ‘.’ pelo número de minas em ladrilhos
    adjacentes.
'''

class Matrix:
    def __init__(self, matrix) -> None:
        self.matrix : list[list[str]] = matrix
        self.shape: tuple = (len(matrix), len(matrix[0]))

    def print_view_minefield(self):
        n, m = self.shape
        mine_field: list[list()] = [[0]*m for i in range(n)] 
        x, y = 0, 0 
        for i in range(n):
            for j in range(m):
                element = self.matrix[i][j]

                if element == "*":
                    x, y = i, j
                    mine_field[i][j] = "*"

                    for j_index in range(y-1, y+2):
                            for i_index in range(x-1, x+2):
                                try:
                                    if mine_field[i_index][j_index] != "*" and i_index >= 0 and j_index >= 0:
                                        mine_field[i_index][j_index] += 1
                                except Exception:
                                    continue

        for row in mine_field:
            for element in row:
                print(f"{element}", end= "")
            print()

n, m = list(map(int, input().split()))
matrix: list[list[str]] = list()

for i in range(n):
    array = list(map(str, input()))
    matrix.append(array)

matrix_obj = Matrix(matrix.copy())
matrix_obj.print_view_minefield()