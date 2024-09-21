import pyfiglet
import random
from game_data import data
# logo of the project
logo = "Higher Lower"
print(pyfiglet.figlet_format(logo))
#logo of versus for player and opponent
art = "v / s"
versus = pyfiglet.figlet_format(art)

# randomly generates data
def random_choice():
    return random.choice(data)

# details of a particular data to give hints about a celeb
def details(random_data):
    name = random_data["name"]
    follower_count = random_data["follower_count"]
    description = random_data["description"]
    country = random_data["country"]

    return f"{name},a {description},from {country}"

# game starts from here
def game():
    current_score = 0 # setting current score as zero for reference
    player_data = random_choice()  # player data is randomly selected by random_choice() function

    game_running = True
    while game_running:
        opponent_data = random_choice()  # let opponent have a random choice

        while opponent_data == player_data: # making sure both player and oppponent data is different
            opponent_data = random_choice()

        player_details = details(player_data)  # details of player
        opponent_details = details(opponent_data)  # details of opponent

        print(f"Compare A : {player_details}")
        print(versus)
        print(f"Against B : {opponent_details}")
        choice = input("\nWho has more followers? Type 'A' or 'B' : ").lower()

        if choice == "q":
            print(f"Thanks for playing ! Final Score = {current_score}\n")
            game_running = False

        elif (choice == "a" and player_data["follower_count"] > opponent_data["follower_count"]) or \
                (choice == "b" and player_data["follower_count"] < opponent_data["follower_count"]):
            current_score += 1
            print(f"You're right ! Current Score = {current_score}\n")
            player_data = opponent_data # setting next player data as opponent data

        else:
            print(f"Better luck next time !!! Final Score : {current_score}")
            game_running = False


game()
