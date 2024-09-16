import pyfiglet

logo = "Tip Calculator"
print(pyfiglet.figlet_format(logo))

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill?\n"))
tip = float(input("What percentage of tip would you like to give? (10, 12, or 15)\n"))
people = int(input("How many people to split the bill?\n"))

# Calculate the total bill including tip
total_bill = bill * (1 + tip / 100)

# Calculate the amount each person should pay
amount_per_person = total_bill / people

# Format the result to 2 decimal places
amount_per_person = round(amount_per_person, 2)

print(f"Each person should pay: ${amount_per_person}")
