"""
This application encrypts and decrypt messages/text according to the shift key
"""
from side import alphabets

# Default displays
print('The text are converted into lower case, be careful not too make a mistake.\n')

# User prompts
text = input("Text to encrypt:\n").lower()
shift = int(input("Type the shift number:\n"))


# Text Encryption


def encrypt(initial_text, shift_num):
    encoding = ""
    for letter in initial_text:
        position = alphabets.index(letter)
        new_position = position + shift_num
        new_letter = alphabets[new_position]
        encoding += new_letter
    print(f'The encoded text is: {encoding}')


encrypt(text, shift)
