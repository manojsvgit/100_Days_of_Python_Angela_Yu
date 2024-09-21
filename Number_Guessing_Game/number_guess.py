import random
import pyfiglet

art = "G U E S S"
print(pyfiglet.figlet_format(art))

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# function to check user guess against actual answer
def check_answer(user_guess, actual_number):
    if user_guess > actual_number:
        print("Too high")
    elif user_guess < actual_number:
        print("Too low")
    else:
        print(f"You got it! The correct answer was {actual_number}")


# function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


# function to handle the game loop
def game():
    # Choosing a number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    print(f"(Psst, the correct answer is {answer})")  # For debugging, can be removed later

    # Set difficulty
    attempts = set_difficulty()
    should_continue = True

    while should_continue:
        guess = int(input("Make a guess: "))
        if guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100.")
            continue

        attempts -= 1
        check_answer(guess, answer)

        if guess == answer:
            should_continue = False
        elif attempts == 0:
            should_continue = False
            print("You've run out of guesses, you lose.")
        else:
            print(f"Guess again. You have {attempts} attempts remaining.")
        print("")

    # Ask if the player wants to play again
    if input("Do you want to play again? Type 'yes' or 'no': ").lower() == "yes":
        game()


# Start the game
game()
