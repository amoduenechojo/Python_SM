player1_input = int(input("Enter rock, paper or scissors: "))
player2_input = int(input("Enter rock, paper or scissors: "))
if player1_input == player2_input:
    print ("TIE")


elif player1_input == "scissors" and player2_input == "paper" :
    print("player1 wins")

elif player2_input == "scissors" and player1_input == "paper" :
    print("player2 wins")

elif player1_input == "rock" and player2_input == "scissors" : 
    print("player1 wins")

elif player1_input == "rocks" and player2_input == "scissors" : 
    print("player2 wins")



else: 
    print ("invalid")
