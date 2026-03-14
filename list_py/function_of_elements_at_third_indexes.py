list_of_numbers = [1, 23, 4, 5, 6, 7, 89]

def adding_third_elements(numbers):

    total = 0
    for index in range(2, len(list_of_numbers), 3):

     total = total + numbers[index]
    return total

adding_third_elements(list_of_numbers)
total = adding_third_elements(list_of_numbers)
print(total)
