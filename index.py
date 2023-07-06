#importing random modules
import random

res=""
def play(user_choice):

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

 print(f"your choice : {user_choice}")
 print(f"computer choice : {computer_choice}")
 print(res)



#score of winners
 user_win=0
 comp_win=0
 draw_win=0

 if res== "match draw":
    draw_win += 1
 elif res == "you win, congratulations!":
    user_win += 1
 else:
    comp_win += 1

 print(f"Score: User-{user_win}, Computer-{comp_win}, Draw-{draw_win}")     

#your choice from input
user_choice = input("please enter you choice(rock,paper,scissor): ")

#quitting game
while user_choice!="quit":
    play(user_choice)
    user_choice=input("please enter you choice(rock,paper,scissor,quit):")

print("thank you for playing")    