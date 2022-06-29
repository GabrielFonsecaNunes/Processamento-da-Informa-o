v = input()

def formatacao_numeros(value: str = None):
    '''
    Args:
        value (str): The input is composed of only an integer greater 
        than zero and less than 1000
    Return:
        The formation of the number in 'hundreds', 'tens' and 'units'. 
    '''
    v = []
    if len(value) == 3:
        v = ['centenas', 'dezenas', 'unidades']
    elif len(value) == 2:
        v = ['dezenas', 'unidades']
    else:
        v = ['unidades']

    f = []

    for i, digit in enumerate(value):
        if i == len(value) - 1:
            if digit != '0':
                f.append(f'{digit} {v[i]}')
        else:
            f.append(f'{digit} {v[i]}')

    
    for i, element in enumerate(f):
        print(element)        
        if i < len(f) - 1:
            print('e')

formatacao_numeros(value = v)