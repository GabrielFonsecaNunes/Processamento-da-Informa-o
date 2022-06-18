c = float(input())

def temperature_conversion(celsius: float = None):
    '''
    Args:
        c (float): The tempurature in Celsius
    Returns:
        t (tuple): The temperature in Fahrenheit and Kelvin 
    '''
    temperature_f = int(1.8 * celsius + 32)
    temperature_k = int(celsius + 273.15)
    t = (f"{temperature_f} F", f"{temperature_k} K")
    return t

for tempurature in temperature_conversion(celsius = c):
    print(tempurature)