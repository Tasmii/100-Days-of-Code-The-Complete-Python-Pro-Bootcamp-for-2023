#This code implements a Caesar cipher, which is a basic encryption technique that involves shifting the letters of the alphabet by a certain amount. 
#The program begins by importing and displaying a logo, which adds a visual element to the application.


from Caesar_Cipher_Logo import logo
print(logo)

def caesar(plain_text, shift_amount, direction_amount):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            if direction_amount == "encode":
                new_position = (position + shift_amount)%26
            elif direction_amount == "decode":
                new_position = (position - shift_amount)%26
            else:
                print("Wrong Direction Input Provided")
            new_letter = alphabet[new_position]
            cipher_text+=new_letter
        else:
            end_text += char
    print(f"The decoded text is {cipher_text}")
should_continue = True
while should_continue:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(plain_text=text, shift_amount=shift, direction_amount=direction)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("GoodBye")
        
#In summary, this code demonstrates a simple implementation of the Caesar cipher, providing an interactive interface for users to encrypt or decrypt messages using a specified shift amount.
