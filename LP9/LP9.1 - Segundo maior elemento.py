'''
Entrada
    A primeira linha da entrada consiste de um único número inteiro N (N ≥ 1) que indica
    o número de linhas da matriz de entrada. Os valores contidos na matriz são apresentados
    nas próximas N linhas da entrada, em que cada linha apresenta os valores contidos em uma
    linha da matriz separados por espaço.
Saída
    A saída do seu programa deve consistir do segundo maior valor da matriz de entrada. Caso a
    matriz não contenha um segundo maior valor, o seu programa deve imprimir “NOT FOUND”.
'''

n = int(input())

m : list[int] = []

for i in range(n):
    m += list(map(int, input().split())) # [int(element) for element in input().split()]

first_max = max(m)

try:
    while first_max in m:
        m.remove(max(m))
    print(max(m))

except Exception:
    print("NOT FOUND")