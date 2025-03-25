# Calculator Program

This is a simple **Python-based calculator** that allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, division, and modulo. The calculator continuously operates until the user decides to start a new calculation.

## Features

- Perform basic arithmetic operations:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`)
  - Modulo (`%`)
- Handles division and modulo by zero.
- Allows continuous calculations with previous results.
- Supports restarting calculations from scratch.

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository or download the script.

```sh
 git clone <repository-url>
```

2. Navigate to the project folder.

```sh
 cd calculator
```

3. Ensure you have Python installed.

```sh
 python --version
```

## How to Run

Run the script using the following command:

```sh
 python calculator.py
```

## Usage

1. Enter the first number.
2. Select an operation from the available options.
3. Enter the second number.
4. The program displays the result.
5. Choose to continue with the result or start a new calculation.

## Error Handling

- **Division by Zero**: Displays `♾️` instead of crashing.
- **Modulo by Zero**: Displays an error message and prevents the operation.
- **Invalid Operation**: Prompts the user to enter a valid operation.

## Example Usage

```
Enter the first number: 10
+
What type of operation you want to perform: +
Enter the second number: 5
10 + 5 = 15.0
Type Y to continue calculating with 15.0 or type 'n' to start new calculation: y
```

## License

This project is licensed under the MIT License.

## Author

Kaif Khan

