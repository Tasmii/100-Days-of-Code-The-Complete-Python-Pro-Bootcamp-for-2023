#The code you provided is a simple bidding program that allows users to enter their names and bid amounts. 
#It determines the highest bidder and displays the winner at the end. 

import os
from art import logo
print(logo)
bids = {}
bidding_finished = False
def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
while not bidding_finished:
    name = input("What is your name?\n")
    price = int(input("What is you bid?\n"))
    bids[name] = price
    should_continue = input("Are there any other bidders?\n")
    if should_continue == "no":
        bidding_finished = True
        highest_bidder(bids)
    elif should_continue == "yes":
        os.system('cls')

#In summary, this code allows multiple users to enter their names and bid amounts. 
#It keeps track of the bids in a dictionary and determines the winner by finding the highest bid. 
#The winner's name and bid amount are then displayed.
