import random
import pyfiglet
from game_data import stages

# Display the Hangman logo
logo = "Hangman"
print(pyfiglet.figlet_format(logo))

# Word list
word_list = ["aarav", "priya", "neha", "rohan", "kavya"]

# Choose a random word
chosen_word = random.choice(word_list)

# Create placeholders for the chosen word
display = "_" * len(chosen_word)
print(display)

# Game variables
game_over = False
correct_letters = set()
lives = 6

# Main game loop
while not game_over:
    guess = input("Guess a letter: ").lower()

    # Check if letter was already guessed
    if guess in correct_letters:
        print(f"You already guessed '{guess}'. Try a different letter.")
        continue

    # Update correct guesses or reduce lives
    if guess in chosen_word:
        correct_letters.add(guess)
        display = "".join([letter if letter in correct_letters else "_" for letter in chosen_word])
        print(display)
    else:
        lives -= 1
        print(f"Incorrect guess. You have {lives} lives left.")

    # Check for game over conditions
    if "_" not in display:
        game_over = True
        print("You Win!")
    elif lives == 0:
        game_over = True
        print(f"You Lose. The word was '{chosen_word}'.")

    # Display current hangman stage
    print(stages[lives])
