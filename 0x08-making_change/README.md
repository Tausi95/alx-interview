---

# Making Change Problem

## Description

The Making Change problem involves determining the fewest number of coins needed to meet a given total using a set of available coin denominations. Given a list of coin denominations and a target total, we need to calculate the minimum number of coins required to meet that total. If it is not possible to achieve the total with the available coins, the function will return `-1`.

### Problem Breakdown:
- You are given a list of coin denominations.
- You need to determine the fewest number of coins required to sum up to a given total.
- If it is impossible to meet the total using any combination of the available coins, return `-1`.
- If the total is `0` or less, return `0` as no coins are needed.

## Requirements

- **Allowed editors**: `vi`, `vim`, `emacs`
- **Python version**: 3.4.3 (on Ubuntu 20.04 LTS)
- **File format**: All your files should end with a new line and should be executable.
- **Code style**: The code should follow PEP 8 style (version 1.7.x).
- **First line in every file**: Should be `#!/usr/bin/python3`.

## Project Structure

```plaintext
.
├── 0-making_change.py  # Function to solve the Making Change problem
└── 0-main.py           # A test script to check the correctness of the solution
```

## Functions

### `makeChange(coins, total)`

This function calculates the fewest number of coins needed to make the given total.

- **Parameters**:
  - `coins` (List): A list of integers representing the coin denominations you have.
  - `total` (Int): The target total amount to make using the coins.
  
- **Returns**:
  - Integer: The fewest number of coins needed to make the total.
  - If it's impossible to make the total with the given coins, it returns `-1`.
  - If the total is `0` or less, it returns `0` (since no coins are needed).

### Example:

```python
makeChange([1, 2, 25], 37)
```
**Output**: 7

Explanation: The fewest number of coins needed to make 37 is 7, which includes 1 coin of 25, 1 coin of 10, 1 coin of 2, and 2 coins of 1.

```python
makeChange([1256, 54, 48, 16, 102], 1453)
```
**Output**: -1

Explanation: It is not possible to make 1453 with the given coin denominations.

## Edge Cases:
- If `total` is `0` or less, return `0` as no coins are needed.
- If no combination of coins can make up the total, return `-1`.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Tausi95/alx-interview.git
   ```

2. Navigate to the project directory:

   ```bash
   cd 0x08-making_change
   ```

3. Make the script executable:

   ```bash
   chmod +x *.py
   ```

## Usage

To run the program and check the correctness of the solution, execute the test script `0-main.py`:

```bash
./0-main.py
```

This script will output the result for the test cases, showing the number of coins needed or `-1` if the total cannot be made.

## License

This project is licensed under the MIT License.

---
