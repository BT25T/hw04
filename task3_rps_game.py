import random

pao = ["rock", "paper", "scissors"]
computer = pao[random.randint(0,2)]

draw = 0
win = 0
com_win = 0

while True:
    player = str(input("rock, paper, scissors or q to quit: ")).lower()
    if player == "q" or player == "quit": break
    if player not in pao:
        print(f"Invalid choice")
        continue
    else:
        print(f"Computer: {computer}")
        if player == computer:
            print("Draw!")
            draw+=1
        elif player == "rock" and computer == "scissors":
            print("You win!")
            win+=1
        elif player == "scissors" and computer == "paper":
            print("You win!")
            win+=1
        elif player == "paper" and computer == "rock":
            print("You win!")
            win+=1
        else:
            print("You lose!")
            com_win+=1
    print(f"You won {win}, the computer won {com_win}, draws: {draw}")