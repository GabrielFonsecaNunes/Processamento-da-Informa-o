import math

r = float(input())

def area(radis: float = None):
    '''
    Args:
        radius (float): It's a radius of circle
    Return:
        area (float): It's area of circle
    '''
    PI = math.pi
    return (PI * r ** 2) 

print(f"{area(radis= r):.4f}")