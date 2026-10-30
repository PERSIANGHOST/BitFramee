while True:
    num1 = input("enter the number: ")
    Mo = input("choice the mathematical operation ( + , - , * , / ): ")
    num2 = input("enter the number: ")

# === کنترل عدد نبودن اینپوت ===
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("please just enter number")
        continue
        
# === عملیات های ریاضی ===
    if Mo == "+":
        result = num1 + num2
    
    elif Mo == "-":
        result = num1 - num2
    
    elif Mo == "*":
        result = num1 * num2
    
    elif Mo == "/":
        if num2 == 0:
            print("you can\'t divide by zero!")
            continue
        else:
            result = num1 / num2
    
    print("Result: ", result)
    choice = input("if you to exit, press (q)!").strip().lower()
    if choice == "q":
        break