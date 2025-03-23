# Silent Bidding System 💰

A simple Python program that allows multiple users to place bids and determines the highest bidder.

## How It Works 🛠
- The program continuously asks users to enter their name and bid amount.
- It stores bids in a dictionary where names are keys and bid amounts are values.
- After all bids are collected, it finds and displays the highest bid and bidder.
- The console is cleared between bids to maintain secrecy.

## Features ✨
- Allows multiple users to place bids.
- Maintains anonymity by clearing previous entries.
- Determines the highest bidder.
- Simple and interactive command-line interface.

## Usage 🚀

### 1. Clone the Repository
```sh
git clone https://github.com/your-username/silent-bidding.git
cd silent-bidding
```

### 2. Install Dependencies (if needed)
Ensure you have Python installed. The program requires the `art` module to display the logo.
```sh
pip install art
```

### 3. Run the Program
```sh
python bidding_system.py
```

### 4. Example Usage
```
What is your name? Alice
What's your bid?: $50
Is there any other user that wants to bid? Type 'Y' for yes and 'N' for no: y

What is your name? Bob
What's your bid?: $70
Is there any other user that wants to bid? Type 'Y' for yes and 'N' for no: n

Bob has the highest bid value $70
```

## Code Overview 📝
```python
from art import logo
print(logo)

def finding_highest_bid(bids):
    highest_bid = 0
    name_value = ""
    for keys in bid_data:
        if bid_data[keys] > highest_bid:
            highest_bid = bid_data[keys]
            name_value = keys
    print(f'{name_value} has the highest bid value ${highest_bid}')

bid_data = {}
bidding = True

while bidding:
    name = str(input("What is your name? "))
    price = int(input("What's your bid?: $"))
    bid_data[name] = price

    user_add = input("Is there any other user that wants to bid? Type 'Y' for yes and 'N' for no: ").lower()
    if user_add == "n":
       bidding = False
       finding_highest_bid(bid_data)
    else:
        print("\n"*100)
```

## Contributing 🤝
Feel free to fork this repository and enhance the bidding system. Pull requests are welcome!

## License 📜
This project is licensed under the MIT License.

---

Enjoy coding! 🚀

