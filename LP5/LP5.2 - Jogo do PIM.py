'''
 Entrada
    O programa recebe um número inteiro maior ou igual a zero.
Saída
    O programa deve mostrar todos os números naturais a partir de 1. Contudo, ao chegar em um 
    múltiplo de 4, o programa deve imprimir a palavra “PIM” e pular uma linha. Veja os exemplos. 
'''

n = int(input())

for i in range(n * 4):
    if (i + 1) % 4 != 0:
        print((i + 1), end= " ")
    else:
        print("PIM", end = " ")
        print("")
