'''
Faça um programa que lê um caractere C (uma string de tamanho 1) e uma string S.
O programa deve imprimir a string S com todos os caracteres C removidos 
(independentemente se estiver maiúsculo ou minúsculo na string).

(Dica: Você pode usar o comando str.lower() para converter uma string str 
para letras minúsculas)
'''

char = input()
expression = input()

expression = expression.replace(char, "")
expression = expression.replace(char.upper(), "")

print(expression)