squares_of_digits = 0
sum_of_digits = 0
factorial_of_digits = 1


user_input = int(input("Enter number :"))

String_number = str(user_input)
for factor in range(len(String_number)):
    index = String_number[factor]
    number = int(index)
    factorial_of_digits += number  
    sum_of_digits +=  factorial_of_digits
 
    print(factorial_of_digits)
 
#print("sum of squares are ",sum_of_digits)
#
#median = []
#sum_of_numbers = 0
#digit_to_be_factored = 1
#digits = int(input("Enter number :"))
#for factors in range(digits):
#    digit_to_be_factored = factors 
#    sum_of_numbers += digit_to_be_factored
#print("Sum of factorial is ",sum_of_numbers)
#
#


 

