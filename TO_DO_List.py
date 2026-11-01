goals = []
while True:
    print("\n===== TO DO LIST =====")
    print("1. Add goal")
    print("2. Show goals")
    print("3. Mark goal as completed")
    print("4. Delete goal")
    print("5. Exit")
    choice = input("Please enter the desired section: ")

# ===================================================


# ===================================================
    if choice == "1":
        goal = input("\nenter your goal: ")
        goals.append(goal)
        print("your goal added!")

    elif choice == "2":
        if not  goals:
            print("You don\'t have a goal yet!")
        else:
            for i, goal in enumerate(goals, start=1):
                print(f"{i}. {goal}")

    elif choice == "3":
        if not  goals:
            print("You don\'t have a goal yet!")
        else:
            for i, goal in enumerate(goals, start=1):
                print(f"{i}. {goal}")

        number = input("\nWhich task did you complete? ")
        

        try:
            number = int(number)
        except ValueError:
            print("Please just enter number!")
            continue
        
        if "completed" in goals[number - 1]:
            print("This goal is already completed!")
            continue
        
        if number < 1 or number > len(goals) :
            print("You don\'t have this goal")
            continue

        goals[number - 1] = goals[number - 1] + " (completed)"

        print("\nupdate goals: ")
        for i, goal in enumerate(goals, start=1):
            print(f"{i}. {goal}")

        
    elif choice == "4":
        if not goals:
            print("You don\'t have a goal yet!")
        else:
            for i, goal in enumerate(goals, start=1):
                print(f"{i}. {goal}")

        number = input("\nwhiche goal do you want delete? ")
        try:
            number = int(number)
        except ValueError:
            print("Please just enter number!")
            continue

        if number < 1 or number > len(goals) :
            print("You don\'t have this goal")
            continue

        goals.pop(number - 1)

        print("update goals: ")
        for i, goal in enumerate(goals, start=1):
            print(f"{i}. {goal}")

    elif choice == "5":
        print("syonara👋")
        break

    else:
        print("please enter valid number!")
        continue