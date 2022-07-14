from random import randint


options = ["rock", "paper", "scissors"]


computer = options[randint(0,2)]

#this line must be set to False
player = False

while player == False:

    player = input("rock, paper, scissors? ")
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player+"!")
        else:
            print("You win!", player, "smashes", computer+'!')
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cuts", player+'!')
        else:
            print("You win!", player, "covers", computer+'!')
    elif player == "scissors":
        if computer == "rock":
            print("You lose...", computer, "smashes", player+'!')
        else:
            print("You win!", player, "cuts", computer+"!")
    else:
        print("That's not a valid play. Check your spelling!")
    #this line can be set to True for a single play or False for unlimted plays
    player = False
    computer = options[randint(0,2)]
