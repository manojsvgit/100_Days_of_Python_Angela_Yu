# Treasure Island Game

----
## Description
Treasure Island is a simple text-based adventure game written in Python. In this game, players make a series of choices to navigate through an adventure and ultimately find the treasure. Each choice leads to different outcomes, and players can either win or lose based on their decisions.

## How to Play
1. **Run the Program**: Execute the Python script in your Python environment.
2. **Follow the Prompts**: You will be prompted to make choices at various stages of the game.
3. **Make Your Choices**: Based on your choices, you will either win or lose.

## Game Flow
1. **First Choice**: Choose between "left" or "right".
   - Choosing "right" results in "Game Over".
   - Choosing "left" allows you to proceed to the next choice.

2. **Second Choice**: If you chose "left", you will be asked to choose between "swim" or "wait".
   - Choosing "swim" results in "Game Over".
   - Choosing "wait" allows you to proceed to the final choice.

3. **Third Choice**: If you chose "wait", you will be asked to choose between "red", "blue", or "yellow".
   - Choosing "yellow" results in "You Win!".
   - Choosing "red" or "blue" results in "Game Over".

## Example
```python
Welcome to Treasure Island
Your mission is to find the treasure.

left or right: left
You Survived

swim or wait: wait
You Survived Again

red, blue, or yellow: yellow
You Win!
```

## Requirements
- Python 3.0

## Installation
1. Clone or download the project files.
2. Run the Python script using the command: 
   ```bash
   python3 treasure_island.py
   ```

## License
This project is open-source and free to use under the MIT License.

------