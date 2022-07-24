'''
Entrada
    Uma string, de no máximo 100 caracteres, que representam os RA's enviados pelo sistema de matrícula.
Saída
    A apresentação da senha provisória ou a indicação de "RA INVALIDO". A senha provisória 
    é formada pelos X caracteres númericos não iniciados em 0 mais à direita da string, por exemplo:
    para o identificador "RA000000000000012340" a senha provisória deve ser "12340". Caso a string 
    recebida não esteja de acordo com as regras de formação, o programa deve indicar "RA INVALIDO".
'''

ra = input()

def check_ra(ra: str = None):
    '''
    Args:
        ra (str) :  
    Returns:
        message (str):
    '''
    if ra.startswith("RA") and len(ra) == 20:
        _ , passoword = ra.split("RA")
        passoword = int(passoword)
        return passoword
    else:
        return "RA INVALIDO"

print(check_ra(ra= ra))