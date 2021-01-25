"""
This application encrypts and decrypt messages/text according to the shift key
"""
from side import alphabets

# Default displays
print('The text are converted into lower case, be careful not too make a mistake.')
print('The shift number must be between 1 and 20.\n')

# User prompts
purpose = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
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

# Text Decryption


def decrypt(encrypt_text, shift_num):
    initial_text = ""
    for letter in encrypt_text:
        position = alphabets.index(letter)
        old_position = position - shift_num
        initial_text += alphabets[old_position]
    print(f"The decoded text is {initial_text}")


if purpose == 'encode':
    # Prevent IndexError
    if (shift < 1) or (shift > 20):
        print('Invalid shift number')
    else:
        encrypt(initial_text=text, shift_num=shift)
elif purpose == 'decode':
    # Prevent IndexError
    if (shift < 1) or (shift > 20):
        print('Invalid shift number')
    else:
        decrypt(encrypt_text=text, shift_num=shift)
else:
    print('Invalid response. Encode or Decode')
