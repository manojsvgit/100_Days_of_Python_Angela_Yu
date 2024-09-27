# ☕ Coffee Machine Game ☕

Welcome to the Coffee Machine Game, where you can brew your favorite coffee just like in real life! Select your drink, insert coins, and enjoy the caffeine buzz. This text-based Python game simulates a coffee vending machine that checks resources, handles money transactions, and brews your chosen drink.

## 🎮 How to Play

1. **Pick your coffee**: The machine offers three choices:
    - `espresso`
    - `latte`
    - `cappuccino`
2. **Check the machine's status**: Type `report` to see how much water, milk, coffee, and money the machine has.
3. **Turn it off**: Type `off` to power down the machine.
4. **Insert coins**: After choosing a drink, insert quarters, dimes, nickels, and pennies. The machine will calculate the total and check if it's enough.
5. **Get your drink**: If enough resources and money are available, the machine will brew your drink and give you change if necessary. If not, it will refund your money or let you know resources are insufficient.

## 💻 How to Run the Game

1. Clone or download this repository.
2. Ensure you have Python 3 installed.
3. In your terminal, navigate to the project folder.
4. Run the game with:
    ```bash
    python coffee_machine.py
    ```
5. Follow the on-screen prompts to select your drink and insert coins.

## 💰 Coin Processing

- **Quarters**: $0.25
- **Dimes**: $0.10
- **Nickels**: $0.05
- **Pennies**: $0.01

Simply enter how many of each coin you are inserting, and the machine will handle the rest.

## 📦 Features

- **Coffee selection**: Choose from espresso, latte, or cappuccino.
- **Resource management**: The machine checks if there's enough water, milk, and coffee to make your drink.
- **Money handling**: Input coins, get change, or be refunded if there's not enough money.
- **Power down**: Turn off the machine anytime by typing `off`.
- **Live report**: View the current resources in the machine with the `report` command.

## 🛠️ Future Features

- Add more drink options like Americano, Mocha, or Macchiato.
- Improve user interface for more intuitive interactions.
- Track and save sales reports to a file.

## 🔗 Example Gameplay

```bash
What would you like? (espresso/latte/cappuccino): latte
Please insert the coins.
How many quarters?: 4
How many dimes?: 1
How many nickels?: 0
How many pennies?: 0
Here is $0.35 in change.
Here is your latte! Enjoy!
