import random
print('''Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.''')

def game_mechanics(difficulty):
    """The whole functionality of game including number of attempts based on the difficulty level"""
    random_number = random.randint(1, 100)
    attempts = 10

    if difficulty == "hard":
        attempts = 5

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a Guess: "))

        if user_guess != random_number:
            attempts -= 1
            if user_guess > random_number:
                print("Too High")
            else:
                print("Too low")

            if attempts == 0: #sometimes there might be attempts = 1 and you guessed incorrectly so the attempt will be reduced by 1 making it zero we need to handle that too
                print(f"Sorry, you ran out of attempts. The correct number was: {random_number}")
                print("Better luck next time! Try again!")
            else:
                print("Make a guess again")
        else:
            print(f"You got it! The answer was {random_number}")
            break

user_difficulty = input("Choose a difficulty: Easy or Hard: ").lower()
if user_difficulty == "easy":
    game_mechanics("easy")
else:
    game_mechanics("hard")
