import random
import pyfiglet
from art import Rock,Paper,Scissor

choices = [Rock, Paper, Scissor]
logo="Rock\nPaper\nScissor"
print(pyfiglet.figlet_format(logo))

print("What do you choose?\nType 0 for Rock\nType 1 for Paper\nType 2 for Scissor")

human_choice = int(input("Enter your choice\n"))  # Convert to integer for correct comparison

print("Your Choice:\n")
print(choices[human_choice])

computer_choice = random.randint(0, 2)
print(f"Computer Choice:\n{choices[computer_choice]}")

# Winning logic
if human_choice == computer_choice:
    print("It's a Draw")
elif (human_choice == 0 and computer_choice == 2) or \
     (human_choice == 1 and computer_choice == 0) or \
     (human_choice == 2 and computer_choice == 1):
    print("You Win!")
else:
    print("You Lost!")
