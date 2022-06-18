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

