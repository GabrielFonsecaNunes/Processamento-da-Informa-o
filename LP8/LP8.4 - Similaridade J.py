'''
Entrada
    Consiste de apenas duas linhas ambas representando um conjunto. A primeira linha corresponde
    ao conjunto A. A segunda linha corresponde ao conjunto B. A separação entre elementos de uma
    lista é dada por um espaço em branco.
Saída
    A saída do seu programa deve apresentar os conjuntos de Interseção e União, ambos ordenados na
    sua forma lexicográfica. A formatação deve seguir os exemplos ilustrados na seguinte tabela. 
'''
a = set(input().split())
b = set(input().split())

inner = " ".join(sorted(a.intersection(b))).strip()
union = " ".join(sorted(a.union(b))).strip()
distance_jaccard = len(a.intersection(b)) / len(a.union(b))

print(f"Intersecao: {inner}")
print(f"Uniao: {union}")
print(f"Similaridade = {distance_jaccard:.2f}")