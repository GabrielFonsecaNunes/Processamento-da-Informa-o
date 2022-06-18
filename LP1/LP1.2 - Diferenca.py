v = []

for i in range(4):
    v.append(int(input()))

def different(vector: list = None):
    '''
    Args:
        vector (list): It's intergers list
    Return:
        dif (int): dif = (vector[0] * vector[1] - vector[2] * vector[3]).
    '''
    dif = (vector[0] * vector[1] - vector[2] * vector[3])

    print(f"DIFERENCA = {dif}")

different(vector = v)