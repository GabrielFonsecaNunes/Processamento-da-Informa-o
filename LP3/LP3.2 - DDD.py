v = input()

def get_state_from_ddd(ddd: str = None):
    '''
    Args:
        ddd (str): It´s DIRECT DIALING DISTANCE ddd
    Return:
        state (str): The name from ddd phone
    '''    
    state ={
            '11': 'Sao Paulo',
            '21': 'Rio de Janeiro',
            '31': 'Belo Horizonte',
            '61': 'Brasilia',
            '71': 'Salvador',
            '32': 'Juiz de Fora',
            '19': 'Campinas',
            '27': 'Vitoria'
    }

    return state[ddd] if ddd in state.keys() else 'DDD nao cadastrado' 

print(get_state_from_ddd(ddd = v))