def calculate_average(numbers)

total_number = 0
length_of_list = 0

    for number in numbers:
        total_number = total_number + number
        length_of_list = length_of_list + 1
  
    average_number = total_number/length_of_list
    return average_number

result = calculating_the_average = [1, 2, 3, 4, 5, 6, 76, 23, 56, 67, 65, 53]
print(result)


def sum_first_middle_last(numbers):

    for index in range(2, len(elements_at_third_indexes), 3):

elements_at_third_indexes = [1, 2, 3, 4, 5, 6, 76, 23, 56, 67, 65, 53]
        elements_at_third_indexes[index] *= 2
print(elements_at_third_indexes)



def find_largest_number(numbers)
largest_number = numbers[0]

    for numbers in numbers: 

        if numbers > largest_number:
            largest_number = number

    return largest_number

numbers_in_list = [12, 34, 56, 1, 7, 9, 3]

result = find_largest_number(numbers_in_list)
print(result) 



def sum_first_middle_last(numbers)
    middle_index = len(number_of_lists) // 2

    first_element = number_of_lists[0]
    middle_element = number_of_lists[middle_index]
    last_element = number_of_lists[-1]

    total = first_element + middle_element + last_element
    return total

number_of_lists = [1, 2, 3, 4, 5, 23, 67, 45, 9]
result = sum_first_middle_last(number_of_lists)

print(result)



list_of_numbers = [1, 23, 4, 5, 6, 7, 89]

def adding_third_elements(numbers):

    total = 0
    for index in range(2, len(list_of_numbers), 3):

     total = total + numbers[index]
    return total

adding_third_elements(list_of_numbers)
total = adding_third_elements(list_of_numbers)
print(total)




def smallest_number(numbers)
    smallest_number = numbers_in_list[0]

    for numbers in numbers: 

        if numbers < smallest_number:
            smallest_number = numbers

numbers_in_list = [12, 34, 56, 1, 7, 0, 3]

result = smallest_number(numbers_in_list)
print(smallest_number)


def even_numbers(numbers)
    total = 0
        
    for number in numbers:
        if number % 2 == 0: 
            total = total + number 

even_indexes = [1, 22, 3, 56, 75, 80]

result = even_numbers(even_indexes)
print(total)

 

def odd_numbers(numbers)
    total = 0
        
    for number in numbers:
        if number % 2 != 0: 
            total = total + number 

odd_indexes = [1, 37, 53, 56, 75, 77]

result = odd_numbers(odd_indexes)
print(result)

 
def true_and_false(arrayNumbers):

    for numbers in range(0, len(arrayNumbers)):
        if arrayNumbers[numbers] % 2 == 0:
            arrayNumbers[numbers] = True

        else: 
            arrayNumbers[numbers] % 2 != 0
            arrayNumbers[numbers] = False
    return arrayNumbers

arrayNumbers = [1,2,3,5,6,7,8,9,0]
print(true_and_false(arrayNumbers))


def zeros_and_ones(arrayNumbers):

    for numbers in range(0, len(arrayNumbers)):
        if arrayNumbers[numbers] % 2 == 0:
            arrayNumbers[numbers] = 1

        else: 
            arrayNumbers[numbers] % 2 != 0
            arrayNumbers[numbers] = 0
    return arrayNumbers

arrayNumbers = [1, 2, 3, 4, 5, 6, 7, 8]
zeros_and_ones(arrayNumbers)



