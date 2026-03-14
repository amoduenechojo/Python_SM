total = 0
for number in range(1,11):
    sum_square_odd_number = int(input("Enter a number: "))
    if(number % 2 != 0):
        square = number * number
        total+= square
        print("The sum square of the odd number is: " , total)
