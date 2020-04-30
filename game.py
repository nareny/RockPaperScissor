import random


def game():
    choices = ["rock", "paper", "scissor"]
    
    print("Rock, paper or scissor?")
    user = input()
    x = random.choice(choices)

    if user == "rock" and x == "rock":
        print("User: Rock")
        print("Computer: Rock")
        print("Equal!")
    elif user == "paper" and x == "rock":
        print("User: Paper")
        print("Computer: Rock")
        print("User wins!")
    elif user == "scissor" and x == "rock":
        print("User: Scissor")
        print("Computer: Rock")
        print("Computer wins!")
    elif user == "rock" and x == "paper":
        print("User: Rock")
        print("Computer: Paper")
        print("Computer wins!")
    elif user == "scissor" and x == "paper":
        print("User: Scissor")
        print("Computer: Paper")
        print("User wins!")
    elif user == "paper" and x == "paper":
        print("User: Paper")
        print("Computer: Paper")
        print("Equal!")
    elif user == "scissor" and x == "scissor":
        print("User: Scissor")
        print("Computer: Scissor")
        print("Equal!")
    elif user == "rock" and x == "scissor":
        print("User: Rock")
        print("Computer: Scissor")
        print("User wins!")
    elif user == "paper" and x == "scissor":
        print("User: Paper")
        print("Computer: Scissor")
        print("Computer wins!")
game()
