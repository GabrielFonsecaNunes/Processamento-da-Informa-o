v = []

for i in range(2):
    v.append(int(input()))

def improper_fractions(v: list = None):
    '''
    Args:
        v (list): It's a list with 2 intergers
    Return
        improper_fractions (str): v[0] / v[1]
    '''
    try:
        r = v[0] // v[1]
        n = v[0] - r * v[1]
        d = v[1]
        return f"{r}({n}/{d})"

    except ZeroDivisionError:
        return "ERRO"

print(improper_fractions(v = v))