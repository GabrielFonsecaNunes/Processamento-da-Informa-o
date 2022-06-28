v = []

for i in range(3):
    v.append(float(input()))

def check_possible_triangle(sides: list = None):
    '''
    Triangle existence condition:
        a < b + c
        b < a + c
        c < a + b
    Args:
        sides (list): It's side of triangle
    Return:
        flag (bool): The outcome if is possible or not to make a triangle
    '''

    for i in range(3):
        for j in range(3):
            for k in range(3):
                if i != j and j != k and i != k:
                    a, b, c = sides[i], sides[j], sides[k]
                    if a >= b + c or a <= 0 or b <= 0 or c <= 0:
                        return False
    return True

def index_element(element, lista: list = None):
    for i, e in enumerate(lista):
        if e == element:
            return i

def is_right_triangle(sides: list = None):
    '''
    Args:
        sides_triangule (float): It's side of triangule
    Return:
        type_triangle (str): The outcome is right triangle or not
    '''
    hip = max(sides)
    index_hip = index_element(element = hip, lista= sides)
    a, b = [sides[i] for i in range(3) if i != index_hip]
    
    if hip**2 == a**2 + b**2:
        return "RETANGULO"

if check_possible_triangle(sides= v):
    print("VALIDO")
    if is_right_triangle(sides= v):
        print("RETANGULO")
else:
    print("INVALIDO")