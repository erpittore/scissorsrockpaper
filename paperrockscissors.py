from random import randint


options = ["rock", "paper", "scissors", 'piedra', 'papel', 'tijera']


computer = options[randint(0,4)]

#this line must be set to False
player = False

while player == False:

    player = input("rock, paper, scissors? ")
    if player == computer:
        print("It is a draw!")
    elif player == "rock" or 'piedra':
        if computer == "paper" or 'papel':
            print("You lose!", computer, "covers", player+"!")
        else:
            print("You win!", player, "smashes", computer+'!')
    elif player == "paper" or 'papel':
        if computer == "scissors" or 'tijera':
            print("You lose!", computer, "cuts", player+'!')
        else:
            print("You win!", player, "covers", computer+'!')
    elif player == "scissors" or 'tijera':
        if computer == "rock" or 'piedra':
            print("You lose...", computer, "smashes", player+'!')
        else:
            print("You win!", player, "cuts", computer+"!")
    else:
        print("That's not a valid play. Check your spelling!")
    #this line can be set to True for a single play or False for unlimted plays
    player = False
    computer = options[randint(0,4)]
