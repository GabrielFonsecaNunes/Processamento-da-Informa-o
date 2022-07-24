'''
Entrada
    A primeira linha contém um número inteiro N (1 < N ≤ 100) representando a quantidade de estímulos em um teste de P300. Cada uma das próximas N linhas consiste de uma string que pode ser apenas uma dentre duas palavras: "ALVO" ou "padrao".
Saída
    A saída é o número M de estímulos alvo contido na sequência de N estímulos. 
'''

n = int(input())
count = 0

for i in range(n):
    if input() == "ALVO":
        count += 1
        
print(count)