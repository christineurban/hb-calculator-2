"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *  #importing everything from arithmetic.py file

def is_valid_operator:
    if tokens[0] !== "+" or !== "-" or !== "*" or !== "/" or !== "square" or !== "cube" or !== "pow" or !== "mod":
        print "You have entered an invalid operation. Please try again."
        continue



using_calculator = True  #while user is inputting operators and numbers


while using_calculator:  

    user_math = raw_input()  #stores input from user as a string

    tokens = user_math.split(" ")  #splits string into list of strings
    
    is_valid_operator(tokens)

    user_numbers = []
    
    for expected_number in tokens[1:]:
        if expected_number.isdigit():
            user_numbers.append(int(tokens[i]))  #converts each index from [1] from a string to an integer
        else:
            print "You have entered an a non-numeric value. Please try again."
            continue 

    if tokens[0] == "+":
        print add(user_numbers)

    elif tokens[0] == "-":
        print subtract(user_numbers)

    elif tokens[0] == "*":
        print multiply(user_numbers)

    elif tokens[0] == "/":
        print divide(user_numbers)

    elif tokens[0] == "square":
        print square(user_numbers)

    elif tokens[0] == "cube":
        print cube(user_numbers)

    elif tokens[0] == "pow":
        print power(user_numbers)

    elif tokens[0] == "mod":
        print mod(user_numbers)

    elif tokens[0] == "q" or tokens[0] == "quit":
        using_calculator = False


quit()  #quits program when while loop is no longer True