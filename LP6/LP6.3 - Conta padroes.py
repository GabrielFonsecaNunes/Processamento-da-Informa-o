'''
Entrada
    A entrada contém duas strings, sem acentos, que podem ter letras 
    maiúsculas ou minúsculas, espaços e caracteres especiais.
Saída
    Seu programa deve imprimir na tela quantas vezes a segunda string
    ocorre dentro da primeira string. 
'''
expression = input()
expression_repeat = input()

def count_pattern_expression(expression:str = None, repeat: str = None):
    c = 0
    for i in range(len(expression) - len(repeat) + 1):
        if expression[i:i + len(repeat)] == repeat:
            c += 1
    return c

print(count_pattern_expression(expression= expression, repeat= expression_repeat))