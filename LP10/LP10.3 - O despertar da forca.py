'''
Entrada
    A primeira linha da entrada tem dois números positivos N e M, representando, respectivamente, o número de linhas e de colunas
    varridos no terreno (3 ≤ N, M ≤ 100). Cada uma das próximas N linhas tem M inteiros, que descrevem os valores lidos em cada célula do terreno.
Saída
    A saída é uma única linha com 2 inteiros X e Y separados por um espaço em branco. Eles representam a coordenada (X, Y) do sabre de luz,
    caso encontrado. Se o terreno não tem um padrão de sabre de luz, X e Y são ambos zero.
'''

class Matrix:
    def __init__(self, matrix) -> None:
        self.matrix : list[list[int]] = matrix
        self.shape: tuple = (len(matrix), len(matrix[0]))

    def find_lightsaber(self) -> str:
        n, m = self.shape

        lightsaber = [[7, 7, 7], [7, 42, 7], [7, 7, 7]]
        x, y = 0, 0
        
        for i in range(n):
            for j in range(m):
                element = self.matrix[i][j]
                if element == 42:
                    try:
                        for i_index, k in enumerate(range(i-1, i+2)):
                            for j_index, w in enumerate(range(j-1, j+2)):
                                value = self.matrix[k][w]
                                lightsaber_value = lightsaber[i_index][j_index]
                                if value != lightsaber_value:
                                    raise Exception
                        
                        x, y = i+1, j+1
                        return f"{x} {y}"

                    except Exception:
                        continue

        return f"{x} {y}"


n, m = list(map(int, input().split()))
matrix: list[list[int]] = list()

for i in range(n):
    array = list(map(int, input().split()))
    matrix.append(array)

matrix_obj = Matrix(matrix.copy())
print(matrix_obj.find_lightsaber())