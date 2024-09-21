# Hangman Game

---

## Description
Hangman is a classic word-guessing game built with Python. The player tries to guess a hidden word by suggesting letters within a limited number of attempts. The game provides visual feedback using stages to indicate the player's progress.

## How to Play
1. Run the game in your Python environment.
2. The program randomly selects a word from the list, and you will see blank spaces representing each letter.
3. Guess a letter by typing it when prompted.
4. If the letter is correct, it will be revealed in the word. If incorrect, you lose a life.
5. The game continues until you either guess the word correctly or run out of lives.

## Example
```python
Welcome to Hangman!
_ _ _ _ _
Guess a letter: a
a _ _ a _
Guess a letter: e
Incorrect guess. You have 5 lives left.
  +---+
  |   |
  O   |
      |
      |
      |
=========
Guess a letter: r
a r _ a _
Guess a letter: v
a r a a v
You Win!


```

## Requirements
- Python 3.0

## Installation
1. Clone or download the project files.
2. Install dependencies using: 

   ```bash
   pip install pyfiglet
   ```
3. Run the Python script using the command: 
   ```bash
   python3 hangman.py
   ```

## License
This project is open-source and free to use under the MIT License.

---