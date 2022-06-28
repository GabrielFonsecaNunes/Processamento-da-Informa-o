v = []

for i in range(5):
    v.append(input())

def evaluation_names(lista: list):
    '''
    Verifica se dentro do array com 5 nomes todos são
    exatamentes iguais
    Args:
        lista(list): Lista com nomes 
    Return:
        flag (bool): Caso todos os nomes forem iguais retorna "Verdadeiro", caso contrario, "Falso" 
    '''
    flag = "Falso"

    for i in range(1, 5):
        anterior = lista[i-1]
        atual = lista[i]
        
        if anterior != atual:
            flag = "Falso"
            return flag

    flag = "Verdadeiro"

    return flag

print(evaluation_names(lista = v))

