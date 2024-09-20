from game_data import MENU, RESOURCES


def report():
    for item, value in RESOURCES.items():
        print(f"{item}: {value}")


def process_coins():
    print("Please insert the coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickle = int(input("How many nickle?: "))
    pennies = int(input("How many pennies?: "))

    total = quarters * (0.25) + dimes * (0.10) + nickle * (0.05) + pennies * (0.01)
    return total


def resource_handle(customer):
    drink = MENU[customer]
    if (RESOURCES["Water"] < drink["ingredients"]["water"]):
        print("Sorry, there is not enough water ")
        return False
    if (RESOURCES["Milk"] < drink["ingredients"]["milk"]):
        print("Sorry, there is not enough milk ")
        return False
    if (RESOURCES["Coffe"] < drink["ingredients"]["coffee"]):
        print("Sorry, there is not enough coffe ")
        return False
    return True


def make_drink(customer):
    drink = MENU[customer]
    RESOURCES["Water"] -= drink["ingredients"]["water"]
    RESOURCES["Milk"] -= drink["ingredients"]["milk"]
    RESOURCES["Coffe"] -= drink["ingredients"]["coffee"]
    RESOURCES["Money"] += drink["cost"]


should_continue = True
while should_continue:

    customer = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    if customer == "report":
        report()
    elif customer == "off":
        print("coffe machine is turned off")
        should_continue = False

    elif customer in ["espresso", "latte", "cappuccino"]:
        if resource_handle(customer):
            total = process_coins()

            if total >= MENU[customer]["cost"]:
                change = total - MENU[customer]["cost"]
                print(f"Here is ${round(change, 2)} in change")
                make_drink(customer)
                print(f"Here is your {customer} Enjoy!")
            else:
                print(f"Sorry that's not enough money.{total} refunded.")
        else:
            print(f"Sorry not enough resources.{customer} refunded.")

    else:
        print("Invalid input. \nPlease choose between espresso, latte, or cappuccino.")
