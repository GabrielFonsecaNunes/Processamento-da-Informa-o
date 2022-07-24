expression = input().lower()
expression = [ch for ch in expression]

vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = [chr(97 + i) for i in range(26) if chr(97 + i) not in vogais]
pontuacoes = [".", ",", "!", "?"]

number_vogais = 0
number_consantes = 0
number_pontuacoes = 0

for vogal in vogais:
    number_vogais += expression.count(vogal)

for consoante in consoantes:
    number_consantes += expression.count(consoante)

for pontuacao in pontuacoes:
    number_pontuacoes += expression.count(pontuacao)

perc_space = expression.count(" ") * 100 / len(expression)
perc_vogal = number_vogais * 100 / len(expression)
perc_consoante = number_consantes * 100 / len(expression)
perc_pontuacao = number_pontuacoes * 100 / len(expression)

print(f"Vogais: {perc_vogal:.2f}%")
print(f"Consoantes: {perc_consoante:.2f}%")
print(f"Espacos: {perc_space:.2f}%")
print(f"Pontuacoes: {perc_pontuacao:.2f}%")