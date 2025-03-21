import random
from hangman_words import word_list
from hangman_art import logo, stages
print(logo)

lives = 6
chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

hints = 0
game_over = False
correct_letters = []
guess_letter = []

while not game_over:

    guess = input("Guess a letter: ").lower()

    if guess in guess_letter :
        print("Try to guess something else")
        continue


    if guess in correct_letters:
        print("You have already guessed that word")
        continue

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        guess_letter.append(guess)
        print(f"You guessed {guess} that's not in the word. You lose a life")


        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word} YOU LOSE******************")
            continue

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])

    print(f"****************************{lives}/6 LIVES LEFT****************************")

    if (lives == 1 or lives ==2) and hints < 2:  # Check if hints are still available
        user_input = input("Do you want a hint? Press Y for yes and N for no: ").upper()

        if user_input == "Y":
            for letter in chosen_word:
                if letter not in correct_letters:
                    print(f"Try Typing: {letter}")
                    hints += 1  # Increment hint count after giving one hint
                    break  # Stop after providing one hint
            if hints == 2:
               print("No more hints available.")

