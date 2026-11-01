import csv

csv_file = input("enter the CSV file path: ")

try:
    with open(csv_file, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(row)

except FileNotFoundError:
    print("File not found! ")

except PermissionError:
    print("You don't have permission to open this file!")