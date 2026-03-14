calculating_the_average = [1, 2, 3, 4, 5, 6, 76, 23, 56, 67, 65, 53]

total_number = 0
average_number = 0
length_of_list = 0

for number in calculating_the_average:
    total_number = total_number + number

    length_of_list = length_of_list + 1
#print(total_number, length_of_list)

average_number = total_number/length_of_list
print(average_number)

