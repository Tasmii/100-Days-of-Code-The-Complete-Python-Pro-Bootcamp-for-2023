#This code implements a simplified version of a blackjack game in Python. It starts by importing necessary modules and defining three functions: deal_card(), compare(), and calculate_score().

#The game begins by dealing two cards each to the player and the computer. While the game is not over, the player is prompted to either draw another card or pass. 
#The player's cards and score are displayed after each move. If the player's score exceeds 21 or they get a blackjack, the game ends.

from art import logo
import random
print (logo)
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, Opponent has Blackjack."
    elif user_score == 0:
        return "Win with a BlackJack."
    elif user_score > 21:
        return "You went over, You lose."
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose."
def calculate_score(cards):
    if sum(cards)==21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
user_cards = []
computer_cards = []
is_game_over = False
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
while is_game_over == False:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer cards: {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
print(f"Your final hand: {user_cards}, final score: {user_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
print(compare(user_score, computer_score))

#Overall, this code allows the user to play a simplified version of blackjack against the computer. 
#The player and computer are dealt cards, and they make decisions to draw cards or pass based on their current scores. 
#The game continues until both players have finished their turns, and the winner is determined by comparing their scores.
