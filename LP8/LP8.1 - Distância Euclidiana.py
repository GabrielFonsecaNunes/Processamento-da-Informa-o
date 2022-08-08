'''
Entrada
    A entrada contém duas linhas representando dois vetores de números reais. Cada número 
    é separado por um espaço em branco.
Saída
    A distância Euclidiana entre ambos os vetores. O número real deve conter apenas 2 casas
    decimais. Caso a dimensão dos vetores forem diferentes a mensagem que deve ser impressa 
    é “ERRO”, sem aspas.
'''
from ast import Break


distance_array_a : list[float] = list(map(float, input().split()))
distance_array_b : list[float] = list(map(float, input().split()))

def euclidiana_distance(array_a : list[float], array_b: list[float]):
    """
    Args:
        array_a (list[float]): _description_
        array_b (list[float]): _description_
    Returns:
        distance (float): _description_
    """
    if len(array_a) != len(array_b):
        return "ERRO"
    
    s = list(map(lambda a, b: (a - b)**2, array_a, array_b))
    distance = round(sum(s)**(1/2), 2)
    return distance

print(f"{euclidiana_distance(distance_array_a, distance_array_b)}")