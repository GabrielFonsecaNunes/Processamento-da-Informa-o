'''
Entrada
    O seu programa deve receber um número inteiro positivo N, que é o tempo inicial do temporizador.
Saída
    Seu deve escrever a saída conforme os exemplos abaixo.
'''
n = int(input())

def crazy_countdown(n: int = None):
    i = 0
    while n >= 0:
        print(f"Faltam {n} segundos")
        i = i + 2
        n = n - i
    print("ACABOU")

def recursive_crazy_countdown(n: int = None, i: int = 0):
    if n >= 0:
        print(f"Faltam {n} segundos")
        i = i + 2
        n = n - i
        return recursive_crazy_countdown(n = n, i = i)
    else:
        print("ACABOU")

recursive_crazy_countdown(n = n)