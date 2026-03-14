

def get_sum_of_two_numbers(first_number, second_number):
    
    if not isinstance(first_number, (int,float)):
        return 0 
    elif not isinstance(second_number, (int,float)):
        return 0    
    return first_number + second_number
    

