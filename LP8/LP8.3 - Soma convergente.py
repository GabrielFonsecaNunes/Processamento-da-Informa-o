'''
Entrada
    A entrada é uma sequência de números inteiros. A sequência sempre terá um número
    par de elementos. Os elementos estão separados estritamente por apenas um espaço 
    em branco.
Saída
    Caso V seja de soma convergente, seu programa deve imprimir “SIM”; caso contrário, 
    “NAO”.
'''
array: list[float] = list(map(float, input().split()))

def is_convergent_sum(array: list[float] = None) -> str:
    """
    Args:
        array (list[float], optional): _description_. Defaults to None.
    Returns:
        bool: _description_
    """
    i = 1
    x = [array[0] + array[-1]]

    while i < len(array) / 2:
        x.append(array[i] + array[-i-1])
        if x[-1] >= x[-2]:
            return "NAO"
        i += 1

    return "SIM"

print(is_convergent_sum(array = array))