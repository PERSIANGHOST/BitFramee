# count text
def count_text(text):
    characters = len(text)
    words = len(text.split())
    lines = len(text.splitlines())
    print(f"Characters : {characters}")
    print(f"Words : {words}")
    print(f"Lines : {lines}")

while True:
    print("\n1. Your text! ")
    print("2. File text! ")
    print("3. Exit")
    choice = input("what do you want? ")

    if choice == "1":
        # your text
        text = input("\nEnter your text: ")
        count_text(text)

    elif choice == "2":
        # file text
        file_path = input("\nEnter your file addres: ")
        try:
            with open(file_path, "r", encoding="utf_8") as file:
                text = file.read()

        except FileNotFoundError:
            print("File not found!")

        except PermissionError:
            print("You don\'t have permission to open this file!")

        else:
            count_text(text)

    elif choice == "3":
        print("sayonara👋👋")
        break

    else:
        print("\nPlease enter value number! ")