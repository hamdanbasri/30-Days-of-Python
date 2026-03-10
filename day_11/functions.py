# Day 11 - Functions

# EXERCISE LEVEL 1

# QUESTION 1
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total
print('QUESTION 1')
print(f'Adding two numbers: {add_two_numbers(1,2)}\n')

# QUESTION 2
def area_of_circle(radius):
    area = 3.14 * radius * radius
    return area
print('QUESTION 2')
print(f'Area of Circle: {area_of_circle(40)}\n')

# QUESTION 3
def add_all_nums(*nums):
    total = 0
    for num in nums:
        # Check if the individual input is an int or float
        if isinstance(num, (int, float)):
            total += num
        else:
            return 'Please input only numbers'
    
    # Return the final sum after the loop finishes
    return total

print('QUESTION 3')
print(f'Adding all numbers: {add_all_nums(2, 3, 5)}\n')

# QUESTION 4
print('QUESTION 4')
celcius = 0
def convert_celcius_to_fahrenheit(celcius):
    fahrenheit = (celcius * (9/5)) + 32
    return fahrenheit

user_input = input("What is the temperature in °C? ")
celcius_val = float(user_input)

print(f'{celcius_val}°C to Fahrenheit (°F) is: {convert_celcius_to_fahrenheit(celcius_val)}°F\n')

# QUESTION 5
print('QUESTION 5')

def check_season(month):
    # It's cleaner to use 'in' for ranges
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer' # Changed from Autumn to Summer for logic!
    elif month in [9, 10, 11]:
        return 'Autumn/Fall'
    else:
        return 'Invalid Month'

# --- The Validation Loop ---
while True:
    user_input = input('What month is it (1-12)? ')
    try:
        month_val = int(user_input)
        # Check if it's a realistic month number
        if 1 <= month_val <= 12:
            break  # Exit the loop because the input is valid
        else:
            print("Please enter a number between 1 and 12.")
    except ValueError:
        print("Invalid input! Please enter a whole number (e.g., 5).")

print(f'The season is: {check_season(month_val)}')
# QUESTION 6
# QUESTION 7
# QUESTION 8
# QUESTION 9
# QUESTION 10
# QUESTION 11
# QUESTION 12
# QUESTION 13
# QUESTION 14
# QUESTION 15