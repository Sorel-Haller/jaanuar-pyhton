import random

while True:

    random_num = random.randint(0, 100)

    input_num = -1

    while input_num != random_num:
        input_num = int(input("Enter number from 1 to 100: "))

        if not (0 <= input_num <= 100):
            print("You have to enter number from 1 to 100!")

        if input_num < random_num:
            print("Too low, try again!")

        else:
            print("Too high, try agin!")    

    print("Correct number!")

    if input("Do you want to play again? y - yes, n - no:").lower() == "n":
        break