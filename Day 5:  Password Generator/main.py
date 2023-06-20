#The provided Python code is a password generator that prompts the user for the desired length of the password, as well as the number of symbols and numbers they want to include. 
#The code then generates a random password based on the given criteria and prints it to the console. 
#Additionally, it shuffles the password to further enhance its randomness and prints the shuffled version as well.

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = ""
for char in range(1, nr_letters+1):
    password += random.choice(letters)
for num in range(1, nr_numbers+1):
    password += random.choice(numbers)
for sym in range(1, nr_symbols+1):
    password += random.choice(symbols)
print(password)

password_list = []
for char in range(1, nr_letters+1):
    password_list += random.choice(letters)
for num in range(1, nr_numbers+1):
    password_list += random.choice(numbers)
for sym in range(1, nr_symbols+1):
    password_list += random.choice(symbols)
random.shuffle(password_list)
new_password=""
for p in password_list:
    new_password+=p
print(new_password)

#Overall, the code provides a simple but effective way to generate random passwords with a mix of letters, symbols, and numbers, and it ensures a certain level of randomness by shuffling the password characters.
