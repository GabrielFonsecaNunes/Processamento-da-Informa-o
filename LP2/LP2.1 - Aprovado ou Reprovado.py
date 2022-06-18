value = str(input())

def evaluation(note: str = None):
    '''
    Args:
        note (str): It's a note, e.g "A", "B"
    Return:
        outcome(str): It´s a outcome  the evalation, e.g approved 
        or disapproved
    '''
    eval_dict = {
                 "A": "APROVADO",
                 "B": "APROVADO",
                 "C": "APROVADO",
                 "D": "APROVADO",
                 "F": "REPROVADO POR DESEMPENHO",
                 "O": "REPROVADO POR FREQUENCIA"
    }
    
    if note in eval_dict.keys():
        return eval_dict[note]
    else:
        return "Conceito invalido!"

print(evaluation(note = value))