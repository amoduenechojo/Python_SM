num_one = int(input("Enter first integer: "))
num_two = int(input("Enter second integer: "))
num_three = int(input("Enter third integer: "))

sum = num_one + num_two + num_three 
print ("sum is: ", sum)

average = sum/3
print ("average: ", average)

product = num_one * num_two * num_three
print ("product is:", product) 

smallest = min(num_one, num_two , num_three)
print("smallest: ", smallest)

largest = max (num_one, num_two , num_three)
print("largest: ", largest)
