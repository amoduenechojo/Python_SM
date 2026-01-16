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
    sum_even = 0

    for i in range(len(number) - 2, -1, - 2):

#            int digit = number.charAt(i) - '0'
        digit = int(number[i]) * 2

        if (digit > 9): 
                digit = digit - 9

        sum_even = sumEven + digit
    return sum_even


def credit_card_validity_status_odd(number):
    number = str(number)
    sum_odd = 0

    for i in range(len(number) - 1, -1, -2):
        sum_odd = sum_odd + int(number[i])

    return sum_odd


def credit_card_validity_status_total(number):
    even = credit_card_validity_status(number)
    odd = credit_card_validity_status_odd(number)
 
    if total % 10 == 0:
        print("Credit card validity status: valid")
    else:
        print("Credit card validity status: invalid")

