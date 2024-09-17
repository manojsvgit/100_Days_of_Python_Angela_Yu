import logo

print(logo.art)
print("Welcome to Treasure Island \nYour mission is to find the treasure.\n")

# First choice
choice1 = input("left or right: ").lower()
if choice1 == "right":
    print("Game Over")
else:
    print("You Survived")

    # Second choice
    choice2 = input("swim or wait: ").lower()
    if choice2 == "swim":
        print("Game Over")
    else:
        print("You Survived Again")

        # Third choice
        choice3 = input("red, blue, or yellow: ").lower()
        if choice3 == "yellow":
            print("You Win!")
        else:
            print("Game Over")
