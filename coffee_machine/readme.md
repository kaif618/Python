# ☕ Coffee Machine Simulator

A fun and interactive **command-line Coffee Machine Simulator** built with Python!  
Simulates a real-world coffee vending machine experience — select a drink, insert coins, manage resources, and enjoy your coffee!

---

## 📜 Features

- ✅ Interactive drink menu with emojis and ASCII art
- 🥤 Supports:
  - **Espresso**
  - **Latte**
  - **Cappuccino**
- 💰 Accepts U.S. coin denominations (quarters, dimes, nickels, pennies)
- 📊 Resource tracking (`water`, `milk`, `coffee`, `money`)
- 🔁 Refill functionality
- 🔌 Option to power off the machine
- 🛠 Developer-friendly modular code structure

---

## 🛠️ Technologies Used

- **Python 3.x**
- CLI (Command Line Interface)
- Modular file structure:
  - `machine_data.py` — Menu and resources
  - `art.py` — Logos and menu art

---

## 📂 Project Structure

```
coffee_machine/
├── main.py               # Main application logic
├── machine_data.py       # Menu items and resource data
├── art.py                # ASCII art for UI
└── README.md             # You're here!
```

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.x installed on your system

### 📦 Installation & Run

```bash
# Clone the repository
git clone https://github.com/yourusername/coffee-machine-simulator.git
cd coffee-machine-simulator

# Run the program
python main.py
```

---

## 🧠 Sample Interaction

```text
📜 Drinks ----- Price
👉 Espresso: $1.5
👉 Latte: $2.5
👉 Cappuccino: $3.0
🤖 What would you like? (espresso/latte/cappuccino): latte
💲 Please Insert coins
🪙 How many quarters: 10
🪙 How many dimes: 0
🪙 How many nickles: 0
🪙 How many pennies: 0
🔄 Here's your $0.0 in change
✅ Here's Your ☕ latte!! Please Enjoy 😄
```

---

## 🧪 Special Commands

- `report` — View machine resources (`water`, `milk`, `coffee`, `money`)
- `refill` — Refill machine supplies (dev/debug mode)
- `off` — Power off the machine

---

## ✨ Credits

- 👨‍💻 Developed with Python
- 🎨 Emojis from [Emojipedia](https://emojipedia.org/)
- 🎨 ASCII art made with love

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

> ☕ “Coffee is a language in itself.” — Jackie Chan  
Enjoy your brew! 🚀
