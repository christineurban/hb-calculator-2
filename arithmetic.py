def add(user_numbers):
    running_total = 0

    for number in user_numbers:
        running_total += number

    return running_total 
            


def subtract(user_numbers):
    running_total = user_numbers[0]

    for number in range(1, (len(user_numbers) - 1)):
        running_total -= number

    return running_total 


def multiply(user_numbers):
    return num1 * num2


def divide(user_numbers):
    # Need to turn at least argument to float for division to
    # not be integer division
    return float(num1) / float(num2) 


def square(num1):
    # Needs only one argument
    return num1 * num1


def cube(num1):
    # Needs only one argument
    return num1 * num1 * num1


def power(user_numbers):
    return num1 ** num2  # ** = exponent operator


def mod(user_numbers):
    return num1 % num2
