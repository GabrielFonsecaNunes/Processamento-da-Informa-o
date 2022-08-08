"""
Entrada
    Cada caso de teste é composto por duas linhas, cada uma contendo uma cadeia de N inteiros. 
    Os valores devem ser separados por um espaço em branco. Não é necessário que as duas cadeias 
    tenham o mesmo número de elementos.
Saída
    Na saída devem ser impressos todos os elementos comuns entre os dois vetores, sendo cada 
    elemento em uma linha diferente. Entretanto, se houver algum elemento que apareça mais de
    uma vez no segundo vetor, o mesmo deve ser impresso apenas uma vez. Se um elemento aparecer 
    mais de uma vez no primeiro vetor, o mesmo pode ser impresso mais de uma vez. Caso não haja 
    nenhum elemento em comum, a seguinte mensagem deverá ser exibida, sem aspas: “NENHUM ELEMENTO 
    EM COMUM”. 
"""
array_a = [int(element) for element in input().split()] 
array_b = [int(element) for element in input().split()] 

def print_inner(array_a: list[int], array_b: list[int]):
    '''
    Args:
        array_a (list[int]):
        array_b (list[int]):
    '''
    inner_array = []

    for element_a in array_a:
        if element_a in array_b:
            inner_array.append(element_a)

    if len(inner_array) == 0:
        print("NENHUM ELEMENTO EM COMUM")
    else:
        for element in inner_array:
            print(element)

print_inner(array_a = array_a, array_b = array_b)