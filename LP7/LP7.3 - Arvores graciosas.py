"""
Entrada
    A primeira linha da entrada consiste de um inteiro n representando o número de 
    vértices da árvore. Cada uma das próximas n – 1 linhas consiste de um par de números 
    inteiros x e y, separados por espaço, indicando que os vértices cuja rotulação atribuiu 
    os números x e y estão ligados por uma aresta. 
Saída
    O seu programa deve imprimir EH GRACIOSA se a rotulação dada for graciosa e NAO EH GRACIOSA 
    caso contrário.
"""

def is_tree_graceful(graph: dict[int:int]) -> bool:
    """
    Args:
        graph (dict[int:int])
    Return:
        flag (bool):
    """
    return False

n = int(input())

# It's a graph
graph : dict[int, int] = dict() 

for i in range(n-1):
    chave, value = [int(element) for element in input().split()]
    graph[chave] = value

print("EH GRACIOSA" if is_tree_graceful(graph= graph) == True else "NAO EH GRACIOSA") 