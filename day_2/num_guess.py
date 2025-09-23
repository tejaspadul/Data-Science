import random

random_number = random.randint(1, 100)
print("Guess the number between 1 and 100!")
while True:
    guess = int(input("Enter your guess: "))
    if guess < random_number:
        print("Too low! Try again.")
    elif guess > random_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it right. The number was {random_number}.")
        break
