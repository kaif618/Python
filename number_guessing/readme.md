# 🎯 Number Guessing Game

Welcome to the **Number Guessing Game**! 🎉 Test your luck and intuition by guessing a random number between **1 and 100**. Can you find the right number before your attempts run out? Let's find out! 🤔💡

---

## 🕹️ How to Play?
1️⃣ Run the game and **choose your difficulty**:
   - 🟢 **Easy Mode** (10 attempts)
   - 🔴 **Hard Mode** (5 attempts)

2️⃣ The game will pick a **random number** between 1 and 100. Your task is to guess it! 🎲

3️⃣ After each guess, the game will give you feedback:
   - 📈 **"Too High"** – Your guess is greater than the correct number.
   - 📉 **"Too Low"** – Your guess is smaller than the correct number.
   - ✅ **"You got it!"** – You guessed correctly!

4️⃣ If you run out of attempts, the game reveals the correct number. 😭

---

## 🏗️ Installation & Running the Game

### 🔧 Prerequisites
- Ensure you have **Python 3** installed on your system.

### ▶️ Running the Game
```sh
python number_guessing_game.py
```

---

## 📜 Code Overview

### **Main Functionality**
- Uses **random.randint(1, 100)** to generate a random number.
- Adjusts **attempts** based on difficulty.
- Provides feedback after each guess.
- Handles **out-of-attempts scenarios** gracefully.

### **Key Features**
✅ Dynamic Difficulty Selection  
✅ Clear User Prompts  
✅ Optimized Guessing Logic  
✅ Encouraging Messages 🎉

---

## 🎥 Demo
🚀 Example Gameplay Output:
```sh
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty: Easy or Hard: easy
You have 10 attempts remaining to guess the number.
Make a Guess: 50
Too High
Make a guess again
You have 9 attempts remaining to guess the number.
Make a Guess: 25
Too Low
Make a guess again
...
You got it! The answer was 42 🎉
```

---

## 🤝 Contributions
Want to enhance this game? Fork the repo, make your improvements, and submit a PR! 🚀

---

## 📜 License
This project is open-source and available under the **MIT License**.

Happy Guessing! 🎲🎯