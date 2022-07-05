n = int(input())
c = input()
array_list = [n, c]

if c in ("TROCA", "INSERE"):
    for i in range(2):
        array_list.append(int(input()))
else:
    array_list.append(int(input()))

def digit_manipulation(array_list: list = None):
    '''
    Args:
        array_list (list): The array list to manipulation number 
    Returns:
        new_digit (int): Return the new digit format as agree expression
    '''
    new_digit = 0
    digit, expression = array_list[0], array_list[1]

    number_digits = 1

    while digit >= 10 ** number_digits - 1:
        number_digits += 1

    if expression == "TROCA":
        index = array_list[2]
        change_number = array_list[-1]
        j = 0

        for i in range(number_digits):
            if i != index - 1:
                last_digit = digit % 10
                new_digit = (last_digit) * 10 ** (j) + new_digit
                j += 1
            else:
                new_digit = (change_number) * 10 ** (j) + new_digit
                j += 1

            digit = digit // 10

    elif expression == "INSERE":
        
        index = array_list[2]
        insert_number = array_list[-1]
        j = 0

        if index <= number_digits:
            for i in range(number_digits + 1):
                if i == index - 1:
                    new_digit = (insert_number) * 10 ** (j) + new_digit
                    j += 1

                else:
                    last_digit = digit % 10
                    new_digit = (last_digit) * 10 ** (j) + new_digit
                    j += 1
                    
                    digit = digit // 10
        else:
            new_digit = insert_number * 10 ** (index - 1) + digit
                

    elif expression == "APAGA":
        index = array_list[-1]
        j = 0

        for i in range(number_digits):
            if i != index - 1:
                last_digit = digit % 10
                new_digit = (last_digit) * 10 ** (j) + new_digit
                j += 1

            digit = digit // 10
        
    return new_digit

print(digit_manipulation(array_list = array_list))