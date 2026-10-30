import random

choices = ["rock", "paper", "scissors"]

while True:
    user = input("Choose rock, paper or scissors: ").strip().lower()

    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print("You : ", user)
    print("Computer : ", computer)

    if user == computer:
        print("This game is a draw.")
    
    elif (user == "rock" and computer == "scissors") or \
        (user == "paper" and computer == "rock") or \
        (user == "scissors" and computer == "paper"):
        print("You Win!🎉")

    else:
        print("You Lose!")

    again = input("dou you want play again? (yes or no): ").strip().lower()

    if again not in ("yes", "y"):
        print("sayonara👋")
        break