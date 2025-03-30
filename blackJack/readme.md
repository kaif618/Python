# 🃏 Blackjack Game

Welcome to the **Blackjack Game** 🎰! This is a simple Python-based terminal game that lets you play Blackjack against the dealer.

## 📌 Features
- 🎴 Random card draws to simulate a real Blackjack game.
- 🃏 Automatic handling of Aces (11 or 1 based on total score).
- 💻 Play against the dealer with realistic AI logic.
- 🏆 Determines winner based on Blackjack rules.

---

## 🚀 How to Play
1. **Run the script** 🖥️:
   ```sh
   python blackjack.py
   ```
2. You'll be asked if you want to play a game of Blackjack.
3. You'll be dealt **two cards** initially, and so will the dealer.
4. Decide whether to **hit (draw another card) or stand (end your turn).**
5. The dealer will then play their turn according to Blackjack rules.
6. The game determines the winner and displays the results!

---

## 🎮 Game Rules
- The goal is to get a **hand value closest to 21** without exceeding it.
- Face cards (K, Q, J) are worth **10 points**.
- Aces can be worth **11 or 1** depending on the total score.
- If you go over 21, you **bust** and lose the round.
- The dealer must **draw cards until reaching at least 17**.
- If both you and the dealer have the same score, it's a **draw**.

---

## 🛠️ Installation & Requirements
This game runs on **Python 3**. If you don’t have Python installed, [download it here](https://www.python.org/downloads/).

To install required dependencies, use:
```sh
pip install art
```

---

## ✨ Example Gameplay
```
Do you want to play a game of Blackjack? Type 'y' or 'n': y

Your cards: [8, 10], current score: 18
Dealer's first card: 7

Type 'y' to get another card, type 'n' to pass: n

Dealer's hand: [7, 9], Score: 16
Dealer draws another card...
Dealer's hand: [7, 9, 5], Score: 21

Dealer wins! 😔 Better luck next time!
```

---

## 📜 License
This game is open-source and free to use under the MIT License.

Happy Playing! 🎲🎉

