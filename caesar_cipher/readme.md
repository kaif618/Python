# Caesar Cipher 🔐

A simple Python implementation of the Caesar cipher for encoding and decoding messages.

## How It Works 🛠

- The user can choose to **encode** (encrypt) or **decode** (decrypt) a message.
- A shift value is provided to shift the letters forward (for encryption) or backward (for decryption).
- Non-alphabet characters remain unchanged.
- The program runs in a loop until the user decides to exit.

## Features ✨

- Handles both uppercase and lowercase letters.
- Preserves non-alphabet characters like spaces and punctuation.
- Works with any shift value, wrapping around the alphabet.
- Simple and easy-to-use interface.

## Usage 🚀

### 1. Clone the Repository

```sh
git clone https://github.com/your-username/caesar-cipher.git
cd caesar-cipher
```

### 2. Install Dependencies (if needed)

Ensure you have Python installed. The program requires the `art` module to display the logo.

```sh
pip install art
```

### 3. Run the Program

```sh
python caesar_cipher.py
```

### 4. Example Usage

```
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello
Type the shift number:
3
Here is the encoded result: khoor
```

### 5. Exiting the Program

To stop running the program, type `no` when prompted:

```
Do you want to go again? Type 'yes' if you want to go again. Otherwise, type 'no'
no
```

## Code Overview 📝

```python
from art import logo
print(logo)
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    str_text = str(original_text)
    for letter in str_text:
        if letter not in alphabet:
            output_text += letter
            continue
        if encode_or_decode == "decode":
            shift_amount *= -1

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

caesar_cipher = True
while caesar_cipher:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    user_input = input("Do you want to go again? Type 'yes' if you want to go again. Otherwise, type 'no' \n")
    if user_input == "yes":
        continue
    else:
        caesar_cipher = False
```

## Contributing 🤝

Feel free to fork this repository and enhance the cipher. Pull requests are welcome!

## License 📜

This project is licensed under the MIT License.

---

Enjoy coding! 🚀

