import random

# Get user-defined limits
lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

# Generate a random number within the range
random_number = random.randint(lower_limit, upper_limit)
print(f"\nGuess the number between {lower_limit} and {upper_limit}!")

# Max attempts
max_chances = 8
chances = 0

while chances < max_chances:
    try:
        guess = int(input(f"\nAttempt {chances + 1} of {max_chances}. Enter your guess: "))
        chances += 1

        if guess == random_number:
            print(f"🎉 Congratulations! You guessed it right. The number was {random_number}.")
            break
        elif guess < random_number:
            print("Too low. Try a higher number.")
        else:
            print("Too high. Try a lower number.")

    except ValueError:
        print("Please enter a valid integer.")

    if chances == max_chances:
        print("\n❌ You've run out of chances.")
        print(f"The number was {random_number}. Better luck next time!")

print("\nThanks for playing!\n")
