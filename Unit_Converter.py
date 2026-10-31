# کنترل ارور در گرفتن عدد در انجام عملیات
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("please enter a valid number!")

############################################
while True:

    print("\n1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Exit")
    choice = input("enter your Unit coice: ")

###########################################
    if choice == "1":
        print("\n1. Meter to Kilometer")
        print("2. Kilometer to Meter")
        print("3. Meter to Centimeter")
        print("4. Centimeter to Meter")

        length_choice = input("Choose a conversion: ").strip()

        if length_choice == "1":
            meter = get_number("Enter the value in meters: ")
            result = meter / 1000
            print(f"{meter} meters = {result} kilometers")

        elif length_choice == "2":
            kilometer = get_number("enter the value in kilometer: ")
            result = kilometer * 1000
            print(f"{kilometer} kilometers = {result} meters")

        elif length_choice == "3":
            meter = get_number("Enter the value in meters: ")
            result = meter * 100
            print(f"{meter} meters = {result} Centimeters")

        elif length_choice == "4":
            centimeter = get_number("Enter the value in Centimeter: ")
            result = centimeter / 100
            print(f"{centimeter} Centimeters = {result} meters")

        else:
            print("Invalid choice!")
            continue

    ####################
    elif choice == "2":
        print("\n1. gram to Kilogram")
        print("2. Kilogram to gram")
        print("3. Pound to Kilogram")
        print("4. Kilogram to Pound")
        weight_choice = input("Choose a conversion: ").strip()

        if weight_choice == "1":
            gram = get_number("enter the desired weight: ")
            result = gram / 1000
            print(f"{gram} grams = {result} kilograms")

        elif weight_choice == "2":
            kilogram = get_number("enter the desired weight: ")
            result = kilogram * 1000
            print(f"{kilogram} kilograms = {result} grams")

        elif weight_choice == "3":
            pound = get_number("enter the desired weight: ")
            result = pound * 0.45359237
            print(f"{pound} pounds = {result} kilograms")

        elif weight_choice == "4":
            kilogram = get_number("enter the desired weight: ")
            result = kilogram / 0.45359237
            print(f"{kilogram} kilograms = {result} pounds")

        else:
            print("Invalid choice!")
            continue

    ####################
    elif choice == "3":
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        temperature_choice = input("Choose a conversion: ").strip()

        if temperature_choice == "1":
            celsius = get_number("enter the desired Temperature: ")
            result = celsius * 9 / 5 + 32
            print(f"{celsius} celsiuss = {result} Fahrenheits")

        elif temperature_choice == "2":
            fahrenheit = get_number("enter the desired Temperature: ")
            result = (fahrenheit - 32) * 5 / 9
            print(f"{fahrenheit} Fahrenheit = {result} Celsius")

        else:
            print("Invalid choice!")
            continue

    ####################
    elif choice == "4":
        print("sayonara👋")
        break

    ####################
    else:
        print("Invalid choice!")
        continue

###########################################
    choice_again = input("\nDo you have any other operations? (Yes or No) ").strip().lower()
    if choice_again not in ("yes", "y"):
        print("sayonara👋")
        break