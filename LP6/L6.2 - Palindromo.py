'''
Entrada
    A entrada contém uma única palavra.
Saída
    O seu programa deve imprimir PALINDROMO, se a palavra recebida for 
    um palíndromo, e NAO EH PALINDROMO, caso contrário.
'''

value = str(input()).upper()
value_reverse = ""

for i in range(len(value) -1, -1, -1):
    value_reverse += value[i]

flag = "PALINDROMO" if value == value_reverse else "NAO EH PALINDROMO"

print(flag)