---

# Prime Game

## Description

The Prime Game is a game where two players, Maria and Ben, take turns choosing a prime number from a set of consecutive integers starting from 1 up to `n`. The chosen prime number and all of its multiples are removed from the set, and the game continues until there are no more prime numbers left for the players to choose. The player who cannot make a move loses the game.

This project implements a solution to determine the winner of multiple rounds of the Prime Game, assuming both players play optimally.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- Python 3.4.3 (Ubuntu 20.04 LTS)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- The code follows PEP 8 style (version 1.7.x)
- All files should be executable

## Project Structure

```plaintext
.
├── 0-prime_game.py      # Contains the implementation of the Prime Game
└── main_0.py            # A script to test the Prime Game
```

## Functions

### `isWinner(x, nums)`

This function determines the winner of the most rounds in the Prime Game.

- **Parameters**:
  - `x`: The number of rounds (integer).
  - `nums`: A list of integers representing the `n` value for each round.
  
- **Returns**:
  - The name of the player who won the most rounds (`'Maria'` or `'Ben'`).
  - If there is no clear winner (both players win an equal number of rounds), the function returns `None`.

### `is_prime(n)`

A helper function that checks if a given number `n` is prime.

- **Parameters**:
  - `n`: The number to check (integer).
  
- **Returns**:
  - `True` if the number is prime.
  - `False` otherwise.

### `play_game(n)`

Simulates a single round of the Prime Game.

- **Parameters**:
  - `n`: The number for that round (integer).
  
- **Returns**:
  - The name of the winner (`'Maria'` or `'Ben'`).

## Example

```python
x = 3
nums = [4, 5, 1]
print(isWinner(x, nums))  # Output: 'Ben'
```

### Round Breakdown:
- **Round 1 (n=4)**:
  - Maria picks 2, removes 2 and 4, leaving 1 and 3.
  - Ben picks 3 and wins because Maria has no more prime numbers to pick.
  
- **Round 2 (n=5)**:
  - Maria picks 2, removes 2 and 4, leaving 1, 3, 5.
  - Ben picks 3, removing 3, leaving 1 and 5.
  - Maria picks 5 and wins because Ben has no more primes to pick.

- **Round 3 (n=1)**:
  - Ben wins because there are no prime numbers for Maria to pick.

In this case, Ben wins 2 rounds, and Maria wins 1 round.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Tausi95/alx-interview.git
   ```

2. Navigate to the project directory:

   ```bash
   cd 0x0A-primegame
   ```

3. Make the scripts executable:

   ```bash
   chmod +x *.py
   ```

## Usage

To run the game and find the winner of a set of rounds, execute the `main_0.py` script:

```bash
./main_0.py
```

The program will output the name of the player who won the most rounds.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
