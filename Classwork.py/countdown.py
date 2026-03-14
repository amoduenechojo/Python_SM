countdown = int(input("Enter the number of asterik: "))
for first_value in range(countdown, 0, -1):
    for value in range(first_value, 0, -1):
        print(value, end = " ")
    print()
