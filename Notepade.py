def show_not():
    try:
        with open("notepade.txt", "r", encoding="utf-8") as file:
            notes = file.readlines()

        if notes:
            print("\n=== Your Notes ===")
            for note in notes:
                print(note, end="")
        else:
            print("\nYou don't have any notes!")

    except FileNotFoundError:
        print("\nFile not found!")

def get_last_num():
    try:
        with open("notepade.txt", "r", encoding="utf-8") as file:
            notes = file.readlines()

        if notes:
            last_note = notes[-1]
            last_num = int(last_note.split(".")[0])
            return last_num

        return 0

    except FileNotFoundError:
        return 0


def new_note():
    num = get_last_num() + 1

    text = input("\nEnter your text: ")

    with open("notepade.txt", "a", encoding="utf-8") as file:
        file.write(f"{num}. {text}\n")

    print("\nNote added successfully!")


def delete_note():
    try:
        with open("notepade.txt", "r", encoding="utf-8") as file:
            notes = file.readlines()

        if not notes:
            print("\nYou don't have any notes!")
            return

        show_not()

        choice = input("\nChoose your note: ")

        try:
            choice = int(choice)
        except ValueError:
            print("\nPlease enter a valid number!")
            return

        note_index = -1

        for i, note in enumerate(notes):
            note_num = int(note.split(".")[0])

            if note_num == choice:
                note_index = i
                break

        if note_index == -1:
            print("\nYou don't have this note!")
            return

        notes.pop(note_index)

        new_note = []

        for i, note in enumerate(notes):
            note_text = note.split(". ", 1)[1]
            new_note.append(f"{i + 1}. {note_text}")

        with open("notepade.txt", "w", encoding="utf-8") as file:
            file.writelines(new_note)

        print("\nNote deleted successfully!")


    except FileNotFoundError:
        print("\nFile not found!")


while True:
    print("\n1. New note")
    print("2. View notes")
    print("3. Delete note")
    print("4. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        new_note()

    elif choice == "2":
        show_not()

    elif choice == "3":
        delete_note()

    elif choice == "4":
        print("\nSayonara 👋")
        break

    else:
        print("\nPlease enter a valid option!")
