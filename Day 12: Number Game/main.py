#This code sets up a Number Guessing Game where the player tries to guess a random number between 1 and 100. 
#The player can choose between Easy and Hard difficulty levels, with Easy providing 10 attempts and Hard providing 5 attempts. 
#After each guess, the program provides feedback to the player, indicating whether the guess is too high, too low, or correct. 
#The game ends when the player either guesses the correct number or runs out of attempts.

from random import randint
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
answer = randint(1, 100)
def attempts():
    global attempt
    difficulty_level=input("Choose a difficulty. Type 'Easy' or 'Hard': ")
    if difficulty_level == "Easy":
        attempt = 10
    elif difficulty_level == "Hard":
        attempt = 5
def check_answer(guess, answer):
    if guess > answer:
        print("Too High")
    elif guess < answer:
        print("Too Low")
    elif guess == answer:
        print(f"You got it! The answer was {answer}.")
        is_game_over = True
is_game_over = False
attempts()
while is_game_over == False:
    print(f"You have {attempt} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    check_answer(guess, answer)
    attempt-=1
    if attempt == 0:
        print("Game over")
        is_game_over = True
