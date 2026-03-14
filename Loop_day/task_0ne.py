
sum_of_all = 0
sum_of_oddSquares = 0
sum_of_squares = 0
mean = 1
sum_of_all = 0
sum_of_even = 0
sum_of_odd = 0
square_of_even= 0
squares_of_odd = 0
for numbers in range(10):
    user_input = int(input("Enter number :"))
    sum_of_all += user_input
    mean = sum_of_all / user_input
    if user_input % 2 == 0:
        print("even ",user_input)
        sum_of_even += user_input
        
        square_of_even = user_input * user_input
        sum_of_squares += square_of_even
    else:
        sum_of_odd += user_input
        print("odd",user_input)
        sum_of_odd += user_input
        squares_of_odd = user_input * user_input
        sum_of_oddSquares += squares_of_odd 


 
sum_of_all =  squares_of_odd + square_of_even
        
print("The Sum of Squares of all  numbers are ",sum_of_all)
 
print("The Sum of Squares of odd numbers are ",sum_of_oddSquares)
 
print("The Sum of Squares of even numbers are ",sum_of_squares)

print("The mean of all numbers are ",mean)

print("The Squares of odd numbers are ",squares_of_odd)

print("The Squares of even numbers are ",square_of_even)

print("The sum of all numbers are ",sum_of_all)

print("The sum of all odd numbers are ",sum_of_odd)
print("The sum of all even numbers are ",sum_of_even)


























