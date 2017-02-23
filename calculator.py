"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *  #importing everything from arithmetic.py file


using_calculator = True  #while user is inputting operators and numbers


while using_calculator:  

    user_math = raw_input()  #stores input from user as a string

    tokens = user_math.split(" ")  #splits string into list of strings

    num1 = int(tokens[1])  #converts first index from a string to an integer
    
    if tokens.len == 3:  #checks if third token exists in list
        num2 = int(tokens[2])  #converts second index from a string to an integer

    if tokens[0] == "+":
        print add(num1, num2)

    elif tokens[0] == "-":
        print subtract(num1, num2)

    elif tokens[0] == "*":
        print multiply(num1, num2)

    elif tokens[0] == "/":
        print divide(float(num1), float(num2))

    elif tokens[0] == "square":
        print square(num1)

    elif tokens[0] == "cube":
        print cube(num1)

    elif tokens[0] == "pow":
        print power(num1, num2)

    elif tokens[0] == "mod":
        print mod(num1, num2)

    elif tokens[0] == "q" or tokens[0] == "quit":
        using_calculator = False


quit()  #quits program when while loop is no longer True