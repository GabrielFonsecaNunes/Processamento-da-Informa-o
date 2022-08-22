'''
Entrada
    Uma linha contendo dois números inteiros separados por um espaço em branco. 
    O primeiro número representa a posição no eixo vertical, o segundo número 
    representa a posição no eixo horizontal. Os números de entrada representam 
    sempre posições válidas (são maiores ou iguais a zero e menores ou iguais a 7).
Saída
    Seu programa deve imprimir todas as possíveis posições do cavalo. A ordem de
    impressão deve respeitar o percurso do tabuleiro de esquerda a direita e de
    cima para baixo.
'''
def horse_moviment(horse_position = list[int]) -> list[list[int]]:
    """
    Args:
        horse_position (_type_, optional): _description_. Defaults to list[int].

    Returns:
        list[list[int]]: _description_
    """
    x, y = horse_position
    moviment_possible: list[list[int]] = list()

    moviments = [[-2, -1], 
                 [-2, 1],
                 [-1, -2],
                 [-1, 2],
                 [1, -2],
                 [1, 2],
                 [2, -1],
                 [2, 1]]
    
    for point in moviments:
        x_p, y_p = point
        if x + x_p >= 0 and x + x_p < 8 and y + y_p >= 0 and y + y_p < 8:
            moviment = [x + x_p, y + y_p]
            moviment_possible.append(moviment)

    return moviment_possible

horse_position: list[int] = list(map(int, input().split())) 

moviments = horse_moviment(horse_position)

for moviment in moviments:
    x, y = moviment
    print(f"{x} {y}") 