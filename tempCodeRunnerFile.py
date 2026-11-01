import random 
import string


while True:
    choic = input("How many values ​​should your password have? ")

    try:
        choic = int(choic)
    except ValueError:
        print("Please enter a number!")
        continue

    try:
        choic < 1
    except ValueError:
        print("please enter one ore upper")
        continue

    characters = string.ascii_letters + string.digits
    password = ""
    for i in range(choic):
        password += random.choice(characters)
    print(password)
    break

