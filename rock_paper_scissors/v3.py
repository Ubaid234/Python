# import random
from random import randint

print("...Rock...")
print("...Paper...")
print("...Scissors...")

player = input("MAKE your Choice: ").lower()
rand_num = randint(0,2)
if rand_num == 0 :
    computer = "rock"
elif rand_num == 1:
    computer = "paper" 
else:
    computer = "scissors"

print(f"Computer plays {computer}")
if player == "rock" and computer == "scissors" :
    print("PLAYER WINS ")
elif player == "rock" and computer == "paper" :
    print("COMPUTER WINS ")
elif player == "paper" and computer == "rock" :
    print("PLAYER WINS ")
elif player == "paper" and computer == "scissors" :
    print("COMPUTER WINS ")
elif player == "scissors" and computer == "rock" :
    print("COMPUTER WINS ")
elif player == "scissors" and computer == "paper" :
    print("PLAYER WINS ")
elif player == computer: 
    print("IT IS A TIE")
else :
    print("SOMETHING IS WRONG")