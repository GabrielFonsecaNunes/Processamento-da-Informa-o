message = input()

def is_request_help(sos_morse: str = None):
    '''
    Args:
        sos_morse (str): It´s a message in morse code
    Return:
        message (str): It's a request for help
    '''
    return "Mensagem com pedido de ajuda!" if '/ ... --- ... /' in sos_morse else "Mensagem sem pedido de ajuda!"

print(is_request_help(sos_morse= message))