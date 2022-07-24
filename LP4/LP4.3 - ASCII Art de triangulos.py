'''
Entrada
    O seu programa receber um número natural N que representa a 
    dimensão (em linhas e colunas) dos lados do triângulo que 
    você deverá desenhar.
Saída
    O seu programa deve desenhar um ASCII Art de um triângulo de 
    dimensão N como demonstrado nos exemplos abaixo.
'''
n = int(input())

for i in range(1, n+1):
    print("*" * i)