import random
import pyfiglet

logo="Password\nGenerator"
print(pyfiglet.figlet_format(logo))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']


print("Welcome to Pypassword Generator!")
enter_letter=int(input("How many letter would you like in passwords?"))
enter_numbers=int(input("How many numbers would you like in passwords?"))
enter_symbols=int(input("How many symbols would you like in passwords?"))

final_password=[]

for letter in range(0,enter_letter):
    final_password.append(random.choice(letters))

for number in range(0,enter_numbers):
    final_password.append(random.choice(numbers))

for symbol in range(0,enter_symbols):
    final_password.append(random.choice(symbols))

print("final passoword without shuffle ",final_password)

random.shuffle(final_password)

print("final passoword with shuffle ",final_password)

password=''
for char in final_password:
    password+=char
print(password)


