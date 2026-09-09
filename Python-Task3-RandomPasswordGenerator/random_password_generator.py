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

        valid_choices = set(choices) & {"1", "2", "3", "4"}

        if len(valid_choices) < 2:
            print("Please select at least 2 valid character types.")
            continue

        character_sets = []

        if "1" in valid_choices:
            character_sets.append(string.ascii_uppercase)

        if "2" in valid_choices:
            character_sets.append(string.ascii_lowercase)

        if "3" in valid_choices:
            character_sets.append(string.digits)

        if "4" in valid_choices:
            character_sets.append(string.punctuation)

        if length < len(character_sets):
            print("Password length is too short for the selected character types.")
            continue

        password = []

        # Add at least one character from every selected type
        for character_set in character_sets:
            password.append(random.choice(character_set))

        # Fill the remaining positions
        all_characters = "".join(character_sets)

        for _ in range(length - len(password)):
            password.append(random.choice(all_characters))

        # Shuffle the password so the required characters are not always at the beginning
        random.shuffle(password)

        password = "".join(password)

        print("\nGenerated Password:", password)

        again = input("\nDo you want to generate another password? (yes/no): ")

        if again.lower() != "yes":
            print("Thank you for using the Random Password Generator!")
            break

    except ValueError:
        print("Please enter a valid number for the password length.")