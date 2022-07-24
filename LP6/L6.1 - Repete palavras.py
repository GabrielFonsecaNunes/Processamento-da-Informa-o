'''
Entrada
    A entrada contém uma palavra, sem acento, que pode ter letras maiúsculas ou minúsculas, e um número inteiro N maior ou igual a zero.
Saída
    O programa deve imprimir N vezes a palavra segundo o formato dado nos exemplos.
'''
word = input()
n = int(input())

try:
    if n > 0:
        expression = f"{word} , " * (n - 1) + f"{word}"
        print(expression)
    else:
        print()
except Exception as e:
    raise e