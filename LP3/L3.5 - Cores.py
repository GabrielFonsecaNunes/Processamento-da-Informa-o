v = ''

for i in range(3):
    v += input()

def mix_color(rgb: str = None):
    '''
    Args:
        list_rgb (list):
    Return:
        color (str):
    '''    
    color ={
            '001': 1,
            '101': 2,
            '100': 3,
            '110': 4,
            '010': 5,
            '011': 6,
            '111': 7,
            '000': 8
    }

    return color[rgb]

print(mix_color(rgb = v))