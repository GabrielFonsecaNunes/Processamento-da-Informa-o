'''
'''
i = int(input())
message = input()

def encode(message: str = None):
    '''
    Args:
        message (str):
    Returns:

    '''
    encode_dict = {}

    for letter in message:
        if letter not in encode_dict.keys():
            encode_dict[letter] = message.count(letter)

    letters_sorted = list(sorted(encode_dict.keys()))
    message_encode = ""
    for letter in letters_sorted:
        n = encode_dict[letter]
        if n >= 3:
            message_encode += f"{letter}{encode_dict[letter]}"
        else:
            message_encode += f"{letter*n}"

    return message_encode

def decode(message: str = None):
    """
    Args:
        message (str):
    Return:
        message_decode (str):
    """
    message_decode = ""

    encode_decode = []

    for i, letter in enumerate(message):
        number = ""

        if letter.isnumeric():
            number += letter
        else:
            if len(number) > 0 and message[i+1]:
                number = int(number)
                encode_decode += message[i-1] * number
                number = ""

    encode_decode

    return message_decode

print(encode(message = message) if i == 1 else (decode(message = message) if i == 2 else "Codigo desconhecido")) 