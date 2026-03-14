positive_number = int(input("Enter a positve number"))

if (number <= 0)
    print("Enter a positive number: ");

else:
    count = 0

    while(number != 1):
        if number % 2 == 0:
            print(number)
        elif number % 3 != 0:
            number = (number // 3) + 1

        count += 1
    print(count)
        
