import random

sign = ["rock", "paper", "scissors"]

while True:

    computer_sign = random.choice(sign)

    user_sign = input ("Enter rock, paper or scissors: ")
    print("computer chose:", computer_sign)

    if user_sign == computer_sign:
        print("It's a tie")

    elif user_sign == "rock":
        if computer_sign == "scissors":
            print("Rock smashes scissors. You win")
        else:
            print ("Paper covers rock. You lose")

    elif user_sign == "paper":
        if computer_sign == "rock":
            print = "Paper cover rock. You win"
        else:
            print = "Scissors cut paper. You lose"


    elif user_sign == "scissors":
        if computer_sign == "paper":
            print = "Scissors cut paper. You win"
        else:
            print = "Rock smashes scissors. You lose"

    if input("Do you want to play again? y - yes, n - no:").lower() == "n":
        break