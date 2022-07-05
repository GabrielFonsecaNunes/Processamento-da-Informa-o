'''
Faça um programa que recebe como entrada a temperatura em graus Celsius 
e realize duas conversões: uma para Fahrenheit e outra para Kelvin.
Entrada:
    A entrada contém um número real representando a temperatura em graus Celsius.
Saída:
    Seu programa deve imprimir na tela dois valores reais arredondados para baixo 
    (use a função int para obter a parte inteira desses valores), sendo o primeiro
    valor a temperatura em Fahrenheit e o segundo valor a temperatura em Kelvin.
'''

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