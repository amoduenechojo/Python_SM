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



