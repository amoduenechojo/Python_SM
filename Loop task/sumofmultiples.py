sum_multiples = int(input("Enter a number: "))
total = 0
for s in range (1, 20001):
    if s % 10 == 0:
            total += 1
            print ("sum: ", total)  

