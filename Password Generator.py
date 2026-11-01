import random 
import string


while True:
    choic = input("How many values ​​should your password have? ")

    try:
        choic = int(choic)
    except ValueError:
        print("Please enter a number!")
        continue

    if choic < 1:
        print("Please enter a positive number!")

    characters = string.ascii_letters + string.digits
    password = ""
    for i in range(choic):
        password += random.choice(characters)
    print(password)

    tryy = input("Do you want try again? (Yes or No) :").strip().lower()
    if tryy not in ("yes", "y"):
        print("sayonara👋")
        break

