print("Welcome to the Tip Calculator!")
amount = input("What was the total bill? ")
percentage = input("What percentage tip would you like to give? ")
people = input("How many people to split the bill? ")
multiplier = float(int(percentage)/100) + 1
tip = ((float(amount)/int(people))*multiplier)
print("Each person should pay: $"+str(round(tip, 2)))
