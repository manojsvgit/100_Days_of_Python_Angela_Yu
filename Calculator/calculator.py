import pyfiglet

# Print calculator banner
print(pyfiglet.figlet_format("Calculator"))

def addition(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    "+": addition,
    "-": substract,
    "*": multiply,
    "/": divide
}

def calculator():
    should_accumulate = True
    num1 = float(input("Enter the first number : "))

    while should_accumulate:
        for thing in operation:
            print(thing)
        operator = input("Choose the Operator : ")
        num2 = float(input("Enter the next number : "))

        answer = operation[operator](num1, num2)
        print(f"{num1}{operator}{num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, 'n' to start a new calculation, or 'exit' to quit: ")

        if choice == "y":
            num1 = answer
        elif choice == "n":
            should_accumulate = False
            print("\n" * 5)
            calculator()  # Restart the calculator
        elif choice == "exit":
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid input. Exiting...")
            break

calculator()
