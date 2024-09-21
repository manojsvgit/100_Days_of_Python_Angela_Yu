import random
import pyfiglet

art="BLACKJACK"
def deal_card():
    '''Returns a random card from deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    '''Takes a list of cards and return the score calculated from cards'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif u_score == 0:
        return "Win with Blackjack"
    elif c_score == 0:
        return "Lose, Opponent has a Blackjack"
    elif u_score > 21:
        return "You went Over. YOU LOSE"
    elif c_score > 21:
        return "Opponent went Over. YOU WIN"
    elif u_score > c_score:
        return "You Win"
    else:
        return "You Lose"

def main_game():
    print(pyfiglet.figlet_format(art))
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1

    def result():
        print(f"Your cards : {user_cards}\tCurrent Score={user_score}")
        print(f"Computers first card : {computer_cards[0]}")

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_over = False
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        result()

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card or 'n' to pass ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print("\n"*2)
    print(f"Yours final hand : {user_cards},final score : {user_score}")
    print(f"Computers final hand : {computer_cards},final score : {computer_score}")
    print("\n")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of blackjack ? Type 'y' or 'n' : ")=="y":
    print("\n"*10)
    main_game()

print("Thank You for playing this game ")