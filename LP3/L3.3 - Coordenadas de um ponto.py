v = []

for i in range(2):
    v.append(float(input()))

def get_quadrant(points: list = None):
    '''
    Args:
        points (list): The points x and y, e.g x, y = (0.1, 0.1)
    Return:
        quadrant (str): The quadrant to which the point belongs 
    '''
    x, y = points

    if x == 0 and y == 0:
        return "Origem"
    elif x != 0 and y == 0:
        return "Eixo X"
    elif x == 0 and y != 0:
        return "Eixo Y"
    elif x > 0 and y > 0:
        return "Q1"
    elif x > 0 and y < 0:
        return "Q4"
    elif x < 0 and y < 0:
        return "Q3"
    else:
        return "Q2"

print(get_quadrant(points= v))