#The provided code is a Python implementation of the classic game Hangman. 
#The game begins by importing the necessary modules, including random for choosing a random word from a predefined list and Hangman_Word and Hangman_Art for accessing the word list and ASCII art, respectively. 
#The code sets up variables such as end_of_game, chosen_word, word_length, and lives to manage the game state and keep track of the player's progress.


import random
from Hangman_Word import word_list
from Hangman_Art import logo, stages

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print(f"You have already guess {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the the word. You lose a life.")
        lives-=1
        if lives == 0:
            end_of_game = True
            print("You Lose!")
            print(f"The word is {chosen_word}.")
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    
    print(stages[lives])

#Overall, this code provides a basic implementation of the Hangman game, allowing players to guess letters and uncover the hidden word.
