def true_and_false(arrayNumbers):

    for numbers in range(0, len(arrayNumbers)):
        if arrayNumbers[numbers] % 2 == 0:
            arrayNumbers[numbers] = True

        else: 
            arrayNumbers[numbers] % 2 != 0
            arrayNumbers[numbers] = False
    return arrayNumbers

#arrayNumbers = [1,2,3,5,6,7,8,9,0]
print(true_and_false(arrayNumbers))



