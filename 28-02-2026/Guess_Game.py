secret = 18;
number = 0;

while(number != -1):
    Guess_Game = int(input("Enter a number: "))

if(number == secret):
    print("You guessed right!")
    break


elif number < secret:
    print("Too low, try again.")


else number > secret:
    print("Too low, try again.")

