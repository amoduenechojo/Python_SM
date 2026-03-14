def even_numbers_list():
    even_number = []
    
    for number in range(0, len()-1):
        if number % 2 == 0:
            even_number.append(number)
    return even_number
