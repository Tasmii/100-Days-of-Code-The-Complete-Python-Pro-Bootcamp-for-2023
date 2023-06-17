#This code is a simple tip calculator that calculates the amount each person should pay based on the total bill, the desired tip percentage, and the number of people splitting the bill. 
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the Tip Calculator!")
amount = input("What was the total bill? ")
percentage = input("What percentage tip would you like to give? ")
people = input("How many people to split the bill? ")
multiplier = float(int(percentage)/100) + 1
tip = ((float(amount)/int(people))*multiplier)
print("Each person should pay: $"+str(round(tip, 2)))
