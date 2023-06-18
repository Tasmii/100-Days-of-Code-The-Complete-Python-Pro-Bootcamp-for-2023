'''Welcome to Treasure Island, an exciting adventure awaits you! Your mission is simple: find the treasure hidden on this mysterious island. Let's get started!

You're standing at a crossroad. Choose either "left" or "right" to determine your path. Type your decision and hit enter.
If you choose the "right" path, you'll come across a lake with an island in the middle. Now, you have two options: "wait" for a boat or "swim" across. Take your pick and type it in.
If you decide to "wait" for the boat, you'll safely reach the island. Ahead of you is a house with three doors: red, yellow, and blue. To find the treasure, choose one door by typing its color.
If you happen to choose the "yellow" door, congratulations! You've found the treasure, and you win the game!
However, if you select any other door, unfortunately, you lose the game. But don't worry, you can always try again for another chance to win.
Enjoy your adventure on Treasure Island and may you discover the hidden treasure!'''

from art import logo
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
Direction = input(print("You are on a crossroad. Where do you want to go? Type \"left\" or \"right\"."))
if(Direction == "right"):
    Lake=input(print("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across."))
    if(Lake == "wait"):
        Door = input(print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which co;our do you choose?"))
        if(Door == "yellow"):
            print("You win")
        else:
            print("You lose. Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")
