print("...Rock...")
print("...Paper...")
print("...Scissors...")

player1 = input("Player1: ")
print(" NO CHEATING\n \n" * 20)
player2 = input("player2: ")

if player1 == "rock" and player2 == "scissors" :
    print("PLAYER1 WINS ")
elif player1 == "rock" and player2 == "paper" :
    print("PLAYER2 WINS ")
elif player1 == "paper" and player2 == "rock" :
    print("PLAYER1 WINS ")
elif player1 == "paper" and player2 == "scissors" :
    print("PLAYER2 WINS ")
elif player1 == "scissors" and player2 == "rock" :
    print("PLAYER2 WINS ")
elif player1 == "scissors" and player2 == "paper" :
    print("PLAYER1 WINS ")
elif player1 == player2: 
    print("IT IS A TIE")
else :
    print("SOMETHING IS WRONG")


