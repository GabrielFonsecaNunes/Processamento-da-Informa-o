'''
Entrada
    O programa recebe um número inteiro, maior ou igual a 1, 
    que indica a dimensão do tabuleiro.
Saída
    O programa deve desenhar o tabuleiro com dois caracteres que
    representam as divisões em cores diferentes conforme exemplos 
    apresentados a seguir.
'''
n = int(input())

def print_chessboard(n: int = None):
    '''
    Args:
        n (int): It's chess board dimension 
    '''
    for i in range(n):
        for j in range(n):
            if (-1)**(i+j) > 0:
                print("o", end="")
            else:
                print("*", end="")
        print()

print_chessboard(n = n)