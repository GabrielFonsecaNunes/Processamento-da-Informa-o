'''
Entrada
    Seu programa receberá uma sequência de inteiros não nulos, um por linha.
Saída
    O número lido, a não ser que seja divisível pelo imediatamente anterior. Quando for, ao invés do número lido, imprima “PUM!” e saia.
'''
v = [int(input())]

def check_puim(n: int = None, m = None):
    '''
    Args:
        n (int): It's a interger number
        m (int): It's a interger number
    Return:
        flag (bool): It's a flag
    '''
    if m % n == 0:
        print("PUM!")
        return True
    else:
        return False    

while True:
    try:
        v.append(int(input()))
        n, m = v[-2], v[-1]
        print(n)
        if check_puim(n = n, m = m):
            break
    except Exception:
        break