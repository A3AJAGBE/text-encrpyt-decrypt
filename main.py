"""
This application encrypts and decrypt messages/text according to the shift number.
The shift number used for encoding must also be used for decoding, otherwise it will not provide a useful information.
"""
from side import alphabetNumeric, logo

# Default displays
print(logo)
print('IMPORTANT:\nThe shift number is vital to encryption and decryption process.\n'
      'The shift number must be between 1 and 20.\n'
      'Keep the shift number safe and separated from the result.')


# The encryption and decryption process
def cipher(initial_text, shift_num, cipher_purpose):
    cipher_text = ""
    if cipher_purpose == "decode":
        shift_num *= -1
    for letter in initial_text:
        # To keep the inputs not in the list
        if letter in alphabetNumeric:
            position = alphabetNumeric.index(letter)
            new_position = position + shift_num
            cipher_text += alphabetNumeric[new_position]
        else:
            cipher_text += letter
    print(f"Here's the {purpose}d result: {cipher_text}")


cipher_continue = True
while cipher_continue:
    # User prompts
    purpose = input("\nDo you want to encrypt? type 'encode' otherwise 'decode' to decrypt:\n").lower()
    text = input(f"Text to {purpose}:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Validating user inputs
    if (purpose == 'encode') or (purpose == 'decode'):
        # Prevent IndexError
        if (shift < 1) or (shift > 20):
            print('Invalid shift number')
        else:
            cipher(initial_text=text, shift_num=shift, cipher_purpose=purpose)
    else:
        print('Invalid response. Encode or Decode')

    restart = input("\nType 'yes' to restart or 'no' to close the program.\n").lower()
    if restart == "yes":
        print('Restarting the application...')
        cipher_continue = True
    elif restart == "no":
        cipher_continue = False
        print("Thank you for using the application.")
    else:
        print('Invalid Response, Restarting the application...')
        cipher_continue = True
