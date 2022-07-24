'''
Entrada
    A entrada contém uma frase sem acentos que pode ter letras maiúsculas ou minúsculas, ou sinais de pontuação.
Saída
    O programa deve imprimir SIM se a frase corresponde a um pantograma. Caso contrário, o programa deve imprimir NAO (sem acento). 
'''
expression = input()

def is_pantograma(message: str = None):
    '''
    '''
    message = message.upper()
    # Alfabeto
    alpha = [chr(65 + i) for i in range(26)]

    for word in alpha:
        if word not in message.upper():
            return "NAO"
    return "SIM"

print(is_pantograma(message = expression))