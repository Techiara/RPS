import random

print("Welcome to Rock, Paper, Scissors!")
def my_game():
    list = ["R", "P", "S"]
    player = False
    computer = random.choice(list)

    player = input("Enter R for Rock , P for Paper, or S for Scissors: ").upper()
    while player not in list:
        print("Invalid input! Try again. ")
        player = input(
            "Enter R for Rock , P for Paper, or S for Scissors: ").upper()
    if player == computer:
        print("Tie!, Here we go again!")
        my_game()    
    elif player == "R":
        if computer == "P":
            print("Computer: ", computer)
            print("Player","(",player,")"," : ","CPU ","(",computer,")")
            print("Computer wins. You lose!")
            print("The game has ended")
        if computer == "S":
            print("Player","(",player,")"," : ","CPU ","(",computer,")")
            print("Computer loses. You win!")
            print("The game has ended")
    elif player == "S":
        if computer == "R":
            print("Player","(",player,")"," : ","CPU ","(",computer,")")
            print("Computer wins. You lose!!")
            print("The game has ended")
        if computer == "P":
            print("Player","(",player,")"," : ","CPU ","(",computer,")")
            print("Computer loses. You win!")
            print("The game has ended")
    elif player == "P":
        if computer == "P":
            print("Player","(",player,")"," : ","CPU ","(",computer,")")
            print("Computer loses. You win!")
            print("The game has ended")
        if computer == "S":
            print("Player","(",player,")"," : ","CPU ","(",computer,")")
            print("Computer wins. You lose!")
            print("The game has ended")
print(my_game())