import random

while True:
    first_dice = random.randint(1,6)
    second_dice = random.randint(1,6)
    user_choice = input("Roll the dice? (y/n): ").lower()
    if user_choice == "y":
        print(f"({first_dice}, {second_dice})")
    elif user_choice == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")
