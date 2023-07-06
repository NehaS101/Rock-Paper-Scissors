#importing random modules
import random

#your choice from input
user_choice = input("please enter you choice(rock,paper,scissor): ")

#computer's choice
choices=["rock", "paper", "scissor"]
computer_choice = random.choice(choices)

#declaring winner according to choice
if user_choice == computer_choice:
    res = "match draw"
elif (user_choice == "rock" or computer_choice == "scissor") or (user_choice == "paper" or computer_choice == "rock") or (user_choice == "scissor" or computer_choice == "paper"):  
    res = "you win, congratulations!"
else:
    res = "computer wins, better luck next time"

    