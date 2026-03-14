def guess_game(number):
    random_number = random.randInt(1, number)
#    guess_game = int(input("Enter a number: "))
     start = 0

    for number in range(start , 3):
        guess_game = int(input("Re-enter a number: "))
    
            if(random_number != guess_game):
                print("You tried!")
           else: 
                print("Good job!")
                break
            if start >=2 :
                random_number = random.randInt(1, number)
                start =0
             

            
