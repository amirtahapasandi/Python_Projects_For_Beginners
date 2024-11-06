from random import randint

random_number = randint(1,100)

while True:
    try:
        user_guess = int(input("Guess the number betwwen 1 and 100: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    if user_guess > random_number:
        print("Too high!")
    elif user_guess < random_number:
        print("Too low!")
    elif user_guess == random_number:
        print("Congratulation! You guessed the number.")
        break
