# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# If another user intends to run this code, they need to make sure they have the "nato_phonetic_alphabet.csv" file in the specified location. 

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv(r"Day 26 Nato Alphabets\nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def generate_phonetics():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetics()
    else:  
        print(output_list)

generate_phonetics()

# This code reads data from a CSV file named "nato_phonetic_alphabet.csv" and creates a dictionary (phonetic_dict) mapping letters to their corresponding NATO phonetic codes. 
# The code then prompts the user to enter a word and converts it to uppercase.
# It retrieves the NATO phonetic code for each letter in the word and stores them in a list (output_list), which is then printed.
