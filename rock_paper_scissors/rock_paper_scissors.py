import random

print("Let's play rock, paper, scissors!")

countForUser = 0
countForComputer = 0

i = 0
while i < 3:
    print("What is your move?")
    stringFromUser = input()
    moveFromUser = str(stringFromUser)
    listOfMoves = ["rock", "paper", "scissors"]
    computerGeneratedMove = random.choice(listOfMoves)
    print(computerGeneratedMove)

    if moveFromUser == computerGeneratedMove:
        print("We got the same move!")

    elif moveFromUser == "rock" and computerGeneratedMove == "paper":
        print("I win this round!")
        countForComputer = countForComputer + 1

    elif moveFromUser == "paper" and computerGeneratedMove == "rock":
        print("You win this round..")
        countForUser = countForUser + 1

    elif moveFromUser == "rock" and computerGeneratedMove == "scissors":
        print("You win this round..")
        countForUser = countForUser + 1

    elif moveFromUser == "scissors" and computerGeneratedMove == "rock":
        print("I win this round!")
        countForComputer = countForComputer + 1

    elif moveFromUser == "paper" and computerGeneratedMove == "scissors":
        print("I win this round!")
        countForComputer = countForComputer + 1

    else:
        print("You win this round..")
        countForUser = countForUser + 1

if countForUser < countForComputer:
    print("I won the game!Ha!")

elif countForComputer < countForUser:
    print("You won the game..")

else:
    print("We are even! Rematch?")
