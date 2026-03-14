#middle index
#number_of_lists = [1, 2, 3, 4, 5, 7, 8, 9]
#
#middle_index = int((len(number_of_lists)/2))
#
#last_index = number_of_lists - 1
#
#first_index = number_of_lists[0]

number_of_lists = [1, 2, 3, 4, 5, 23, 67, 45, 9]

middle_index = len(number_of_lists) // 2

first_element = number_of_lists[0]
middle_element = number_of_lists[middle_index]
last_element = number_of_lists[-1]

total = first_element + middle_element + last_element

print(total)

