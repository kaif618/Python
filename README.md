# Python
Python 100 days challenge
<br>
Day1 : Made a Band Name Generator, Tip Calculator Project
<br>
Day2 : Rollercoaster file
<br>
Day3 : Treasure island
<br>
Day4 : Rock paper and scissor
<br>
Day5: Random Password Generator
<br>
Day6: Hangman game

# Rock Paper Scissors Game 🎮

This is a simple **Rock, Paper, Scissors** game written in Python. The player competes against the computer in a classic showdown of luck and strategy!

## How It Works 🛠️

- The player selects **Rock (0), Paper (1), or Scissors (2)**.
- The computer randomly chooses one of the three options.
- The winner is determined based on the standard Rock-Paper-Scissors rules:
  - **Rock beats Scissors** 🏆
  - **Paper beats Rock** 🏆
  - **Scissors beats Paper** 🏆
  - Same choices result in a **Draw** 🤝
  
## How to Run 🏃‍♂️

1. Make sure you have Python installed (`Python 3.x` recommended).
2. Clone this repository or download the script.
3. Run the script in your terminal:

   ```bash
   python rock_paper_scissors.py

Features ✨
✅ Random computer selection
✅ ASCII art representation
✅ Simple and fun to play!

Enjoy playing and feel free to improve the game! 🚀

# PyPassword Generator 🔒  

A simple Python script to generate a random password with user-specified numbers of letters, symbols, and digits.

## 🚀 Features
- Generates a random password with a mix of **letters**, **numbers**, and **symbols**.
- Ensures characters are **shuffled** to avoid predictable patterns.
- Allows the user to specify the number of each type of character.
- Easy-to-use **command-line interface**.

## 🛠️ How It Works
1. The script asks the user for the number of letters, symbols, and numbers they want in their password.
2. It randomly selects characters based on the input.
3. It shuffles the selected characters to ensure randomness.
4. The final password is displayed on the screen.

## 📜 Usage
Run the script using Python:
```sh
python password_generator.py

📌Notes
1. Each password is unique and randomly generated.
2. If you prefer a longer or shorter password, just change the input values when prompted.
3. This script does not store or save passwords for security reasons.

```markdown
# Hangman Game

Welcome to the **Hangman Game** – a classic command-line game built with Python! Test your word-guessing skills and challenge yourself to figure out the secret word before you run out of lives.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Game Structure](#game-structure)


---

## Overview

This Hangman game selects a random word from a list and prompts you to guess letters one at a time. With each incorrect guess, you lose a life and see the corresponding stage of ASCII art. Can you guess the word before all lives are lost?

---

## Features

- **Interactive Gameplay:** Input a letter at a time and see the game update live.
- **Dynamic ASCII Art:** Visual representation of your remaining lives.
- **Random Word Selection:** Each session picks a new word from the list.
- **User Feedback:** Informs you of correct guesses, repeated letters, and wrong attempts.

---

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your_username/your_repo.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd your_repo/hangman_game
   ```

3. **Ensure Python 3.6+ is Installed:**  
   Verify with:
   ```bash
   python --version
   ```
   If needed, [download Python](https://www.python.org/downloads/).

---

## Usage

1. Open your terminal in the `hangman_game` directory.
2. Run the game:
   
   ```bash
   python hangman.py
   ```

3. Follow the on-screen instructions to guess letters. You have **6 lives** – each incorrect guess reduces your lives. Keep guessing until you either reveal the word or run out of lives!

---

## Game Structure

- **hangman.py:** Main game script containing the game loop and logic.
- **hangman_words.py:** Contains the list of words used for the game.
- **hangman_art.py:** Contains the ASCII art for the game logo and life stages.

---

### Instructions:
- **Replace** `your_username` and `your_repo` with your actual GitHub username and repository name.
- **Add a screenshot** by placing an image named `screenshot.png` in your repository or updating the image URL as needed.
- **Customize further** if you have additional sections or badges you want to include.
