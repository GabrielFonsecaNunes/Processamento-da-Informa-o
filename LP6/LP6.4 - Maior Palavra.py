'''
Entrada
    A primeira linha da entrada consiste de um único número inteiro 
    que representa o número de linhas do texto.
    As próximas N linhas contém as linhas do texto.

Saída
    A sua saída deve consistir de uma única linha contendo a frase 
    Tam. Maior Palavra: seguido do número de caracteres da maior palavra 
    (separados por espaço).
'''
array = []
n = int(input())

for i in range(n):
    array.extend(input().split(" "))

big_word = ""

for word in array:
    if len(word) > len(big_word):
        big_word = word

print(f'Tam. Maior Palavra: {len(big_word)}')