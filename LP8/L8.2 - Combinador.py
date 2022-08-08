'''
Entrada
    Cada caso de teste é composto por uma linha que contém duas cadeias de caracteres, separadas por um espaço em branco. Cada cadeia de caracteres deve conter entre 1 e 50 caracteres inclusive.
Saída
    Combine as duas cadeias de caracteres da entrada como mostrado no exemplo abaixo e exiba a cadeia resultante.
'''
message = input()

i = 0
j = 0

expressions = message.split()
word_a = expressions[0]
word_b = expressions[1]
expression = ""

while i < len(word_a) or j < len(word_b):
    if i < len(word_a):
        expression += word_a[i]
        i += 1
    if j < len(word_b):
        expression += word_b[j]
        j += 1

print(expression)