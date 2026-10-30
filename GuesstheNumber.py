import time
import random

print("Welcome to Guess the Number!😉")
time.sleep(1)
print("I'm thinking of a number between 1 and 10.")
time.sleep(1)
print("try to find it😁")
time.sleep(1)

while True:
    attempts = 0
    number = random.randint(1, 10)

    while True:

        try:
            guess = int(input("Guess the number:"))
            attempts += 1

            if guess < number:
                print("too lower. try again!")

            elif guess > number:
                print("too high. try again!")

            else:
                print("Congratulations! You guessed it!")
                print("number of attempts: ", attempts)
                break

        except ValueError:
            print("please enter value number!!!")

    time.sleep(1)
    choice = input("do you want play again?(Yes , No)").strip().lower()
    if choice != "yes" and choice != "y":
        break
    else:
        continue