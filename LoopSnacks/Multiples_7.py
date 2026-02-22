count = 0
for number in range (1, 101):
    if(number % 7 == 0):
        count = count + 1
print("There are", count, "numbers divisible by 7 between 1 and 100")
