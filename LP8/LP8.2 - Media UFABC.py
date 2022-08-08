'''
Entrada
    A entrada consiste de uma única linha contendo a nota que o aluno recebeu em cada 
    uma das listas, separadas por espaço. Cada nota consiste de um número real e você 
    pode assumir que o professor aplicou pelo menos 3 listas de exercício.
Saída
    A saída do seu programa deve consistir de uma única linha contendo a frase “MEDIA FINAL:”,
    seguida da média final do aluno, separados por espaço. A média final deve ser apresentada 
    com quatro casas decimais de precisão.
'''
array_a: list[float] = list(map(float, input().split()))
max_value = float(max(array_a))
min_value = float(min(array_a))
array_a.remove(max_value)
array_a.remove(min_value)

mean_array = sum(array_a) / len(array_a)
print(f"MEDIA FINAL: {mean_array:.4f}")