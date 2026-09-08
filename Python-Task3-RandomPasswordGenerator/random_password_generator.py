import random
import string

print("Random Password Generator")
while True:
    try:
        length = int(input("Enter the length of the password (minimum 8): "))
        if length < 8:
            print("Password length must be at least 8 characters.")
            continue

        print("\nChoose character types:")
        print("1. Uppercase letters")
        print("2. Lowercase letters")
        print("3. Numbers")
        print("4. Symbols")

        choices = input("Enter at least 2 choices (example: 123): ")

        characters = ""

        if "1" in choices:
            characters += string.ascii_uppercase

        if "2" in choices:
            characters += string.ascii_lowercase

        if "3" in choices:
            characters += string.digits

        if "4" in choices:
            characters += string.punctuation

        if len(set(choices)) < 2:
            print("Please select at least 2 different character types.")
            continue

        if characters == "":
            print("Please select valid character types.")
            continue

        password = ''.join(random.choice(characters) for i in range(length))

        print("\nGenerated Password:", password)

        again = input("\nDo you want to generate another password? (yes/no): ")

        if again.lower() != "yes":
            print("Thank you for using the Random Password Generator!")
            break

    except ValueError:
        print("Please enter a valid number for the password length.")