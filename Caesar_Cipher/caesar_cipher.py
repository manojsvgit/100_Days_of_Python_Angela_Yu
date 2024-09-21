import pyfiglet

text = "caesar cipher 3"
ascii_art = pyfiglet.figlet_format(text)
print(ascii_art)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, decode_encode):
    if decode_encode == "decode":
        shift_amount = shift_amount * (-1)

    caesar_text = ""
    for char in original_text:
        if char not in alphabet:
            caesar_text += char
        else:
            shifted_index = alphabet.index(char) + shift_amount
            shifted_index %= len(alphabet)
            caesar_text += alphabet[shifted_index]

    print(caesar_text)


should_continue = True

while should_continue:
    direction = input("encode/decode: ")
    text = input("Your message: ").lower()
    shift = int(input("Shift number: "))

    caesar(original_text=text, shift_amount=shift, decode_encode=direction)

    restart = input("\nType 'yes' if you want to continue, type 'no' to end: \n")
    if restart == "no":
        should_continue = False
        print("Goodbye!")
