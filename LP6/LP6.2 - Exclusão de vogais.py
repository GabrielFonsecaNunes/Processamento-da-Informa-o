'''
Entrada
    A entrada contém uma única string, sem acento, que pode ter letras 
    maiúsculas ou minúsculas.
Saída
    Seu programa deve imprimir na tela a string resultante da exclusão de 
    todas as suas vogais. Se o usuário digitar uma palavra que contém apenas
    vogais, o programa deve imprimir a string vazia (“”), o que corresponde 
    a uma saída “em branco”.
'''

vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
expression = input()

for vogal in vogais:
    expression = expression.replace(vogal, "")

print(expression)