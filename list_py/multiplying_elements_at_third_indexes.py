elements_at_third_indexes = [1, 2, 3, 4, 5, 6, 76, 23, 56, 67, 65, 53]

for index in range(2, len(elements_at_third_indexes), 3):
#    if elements_at_third_indexes == number[2]:
        elements_at_third_indexes[index] *= 2
print(elements_at_third_indexes)

