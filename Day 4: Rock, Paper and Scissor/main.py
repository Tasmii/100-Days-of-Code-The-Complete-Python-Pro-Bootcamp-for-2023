'''The provided code is a basic implementation of the rock-paper-scissors game between a user and the computer. 
It starts by importing the necessary random module and defining ASCII art representations for the rock, paper, and scissors choices. 
These ASCII art images are stored in a list called game_images.'''


import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice>2 or user_choice<0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0,2)
    print("Computer Choice")
    print(game_images[computer_choice])
    if user_choice == 0 and computer_choice == 2:
        print("You Win")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose")
    elif user_choice > computer_choice:
        print("You Win")
    elif computer_choice > user_choice:
        print("You Lose")
    elif computer_choice == user_choice:
        print("It's a draw")
        
'''In summary, this code allows the user to play a single round of rock-paper-scissors against the computer and provides visual representation of the choices made. 
It determines the winner based on the game rules and displays the outcome accordingly.'''
