def add(user_numbers):
    """Takes a list of integers of any length and adds them together, returning result as single integer output"""
    running_total = 0
    for number in user_numbers:
        running_total += number
    return running_total


def subtract(user_numbers):
    """Takes a list of integers of any length and subtracts each subsequent value from the previous running total, returning result as single integer output"""
    running_total = user_numbers[0]
    for number in user_numbers[1:]:
        running_total -= number
    return running_total


# below observe range version of subtract function
#
#  def subtract(user_numbers):
#     running_total = user_numbers[0]
#     for index in range(1, (len(user_numbers))):
#         running_total -= user_numbers[index]
#     return running_total 


def multiply(user_numbers):
    """Takes a list of integers of any length and multiplies them together, returning result as single integer output"""
    running_total = user_numbers[0]
    for number in user_numbers[1:]:
        running_total *= number
    return running_total


def divide(user_numbers):
    """Takes a list of integers of any length and divides previous running total by each subsequent value, returning result as single float output"""
    running_total = float(user_numbers[0])
    for number in user_numbers[1:]:
        running_total /= float(number)
    return running_total


def square(user_numbers):
    """Takes a list of integers of any length and multiplies the squares of each integer together, returning result as single integer output"""
    running_total = user_numbers[0] ** 2
    for number in user_numbers[1:]:
        running_total *= number ** 2
    return running_total


def cube(user_numbers):
    """Takes a list of integers of any length and multiplies the cubes of each integer together, returning result as single integer output"""
    running_total = user_numbers[0] ** 3
    for number in user_numbers[1:]:
        running_total *= number ** 3
    return running_total


def power(user_numbers):
    """Takes a list of integers of any length and raises the running total to the power of each subsequent value, returning result as single integer output"""
    running_total = user_numbers[0]
    for number in user_numbers[1:]:
        running_total **= number
    return running_total


def mod(user_numbers):
    """Takes a list of integers of any length takes the modulus of the running total and each subsequent number, returning result as single integer output"""
    running_total = user_numbers[0]
    for number in user_numbers[1:]:
        running_total %= number
    return running_total
