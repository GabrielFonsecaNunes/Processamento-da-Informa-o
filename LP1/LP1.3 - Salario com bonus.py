'''
Faça um programa que leia o nome de um vendedor, o seu salário fixo e 
o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que
este vendedor ganha 5% de comissão sobre suas vendas efetuadas, informar
o total a receber no final do mês, com duas casas decimais.
Entrada:
    A entrada contém um texto (primeiro nome do vendedor) e 2 números 
    reais com duas casas decimais, representando o salário fixo do 
    vendedor e montante total das vendas efetuadas por este vendedor, 
    respectivamente.
Saída:
    Seu programa deve imprimir na tela o total que o funcionário 
    deverá receber, conforme exemplo fornecido.
'''

v = [input()]

for i in range(2):
    v.append(float(input()))

def describe_salary(info: list = None):
    '''
    Args:
        info (list): It's list 
    Return:
        bonus (str): 
    '''
    salary_with_bonus = info[1] + info[2] * 0.05
    print(f"{info[0]} deve receber R$ {salary_with_bonus:.2f}")

describe_salary(info= v)

