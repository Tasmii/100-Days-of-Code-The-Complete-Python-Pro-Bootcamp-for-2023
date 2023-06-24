#The given code is an implementation of a simple calculator using Python. 
#It defines several mathematical operations such as addition, subtraction, multiplication, and division as separate functions. 
#These functions take two numbers as input and perform the corresponding operation on them, returning the result.

from art import logo
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = float(calculation_function(num1, num2))

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")== "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()


#Overall, this code provides a basic calculator functionality that allows users to perform consecutive calculations without terminating the program. 
#It demonstrates the use of functions, dictionaries, loops, and user input/output handling in Python.
