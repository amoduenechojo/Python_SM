def credit_card_digit_length(number):
    
    length = len(str(number))    
    number = str(5482707943)
    if number >= 13 and number <= 16: 
            print("Credit card digit length: Valid")
    else: 
            print("Credit card digit length: Invalid")
 
def card_type(number):
    number = str(number)

    if str(number).startswith("4"): 
        print("Credit card type: Visa Card")  


    elif str(number).startswith("5"):
        print("Credit card type: Master card")


    elif str(number).startswith("37"):
        print("Credit card type: American express card")


    elif str(number).startswith("6"):
        print("Credit card type: Discover card")


    else:
        print("Credit card type: Invalid")


def credit_card_validity_status(number):
    number = str(number)
    sum_of_even_position = 0

    for index in range(len(number) - 2, -1, - 2):

        digit = int(number[index]) * 2

        if (digit > 9): 
                digit = digit - 9

        sum_of_even_position = sumEven + digit
    return sum_of_even_position


def credit_card_validity_status_odd(number):
    number = str(number)
    sum_of_odd_position = 0

    for index in range(len(number) - 1, -1, -2):
        sum_of_odd_position = sum_of_odd_position + int(number[index])

    return sum_of_odd_position


def credit_card_validity_status_total(number):
    even = credit_card_validity_status(number)
    odd = credit_card_validity_status_odd(number)
 
    if total % 10 == 0:
        print("Credit card validity status: valid")
    else:
        print("Credit card validity status: invalid")

