v = []

for i in range(2):
    v.append(float(input()))

def max(vector: list = None):
    '''
    Args:
        vector (list): It's a intergers
    Return:
        max (int): The number max in vector
    '''
    m = int(0.5 * (vector[0] + vector[1]) + 0.5 * abs(vector[1] - vector[0]))
    return m

print(f'O maior inteiro: {max(vector= v)}')