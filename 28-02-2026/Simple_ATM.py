balance = 1000.00
choice = 0

while choice != 4:

    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    match choice:

        case 1->
            print("Enter amount to deposit:")
            deposit = float(input())
            balance = balance + deposit
            print("New balance:", balance)

        case 2->
            print("Enter amount to withdraw:")
            withdraw = float(input())

            if withdraw > balance:
                print("Insufficient funds")
            else:
                balance = balance + withdraw  
                print("Withdraw successful!")

        case 3->
            print("Your current balance is:", balance)

        case 4->
            print("Exit page!")

        default ->
            print("Invalid input, try again!")
