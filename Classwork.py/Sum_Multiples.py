Sum_multiples = int(input("Enter a number: "))
total = 0
for number in range (1, 20001):

    if number % 10 == 0:
            total = total +  1
            print ("sum: ", total)  

