# Day 11 - Functions

# EXERCISE LEVEL 1

# QUESTION 1
print('QUESTION 1')
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total
print(f'Adding two numbers: {add_two_numbers(1,2)}\n')

# QUESTION 2
print('QUESTION 2')
def area_of_circle(radius):
    area = 3.14 * radius * radius
    return area
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

print(f'The season is: {check_season(month_val)}\n')

# QUESTION 6
print('QUESTION 6')
slope_output = 0
def calculate_slope(x1, x2, y1, y2):
    slope = (y2 - y1) / (x2 - x1)
    slope_output = slope
    return slope

print(f'The slope is valued at: {calculate_slope(20,2,33,4)}\n')

# QUESTION 7
print('QUESTION 7')
def solve_quadratic_eqn(a, b, c):
    if a == 0:
        return "This is a linear equation, not quadratic (a cannot be 0)."

    # Calculate the discriminant
    d = b**2 - 4*a*c
    
    if d > 0:
        # Two real solutions
        sol1 = (-b + (d**0.5)) / (2 * a)
        sol2 = (-b - (d**0.5)) / (2 * a)
        return {sol1, sol2}
    
    elif d == 0:
        # One real solution
        sol = -b / (2 * a)
        return {sol}
    
    else:
        # For complex numbers, we use the absolute value of d
        # and Python's 'j' for the imaginary part
        real_part = -b / (2 * a)
        imag_part = (abs(d)**0.5) / (2 * a)
        return {complex(real_part, imag_part), complex(real_part, -imag_part)}

# Example: x^2 - 3x + 2 = 0
print(f"Solutions: {solve_quadratic_eqn(1, -3, 2)}\n")

# QUESTION 8
print('QUESTION 8')

def print_list(my_list):
    for element in my_list:
        print(element)

tech_stack = ['Python', 'JavaScript', 'SQL', 'HTML']
print(f'{print_list(tech_stack)}\n')

# QUESTION 9
print('QUESTION 9')
def reverse_list(*numbers):
    num_list = list(numbers)
    num_list.reverse()
    return num_list

print(reverse_list(1, 2, 3, 4, 5))
print(f'{reverse_list("A", "B", "C")}\n') 

# QUESTION 10
print('QUESTION 10')
def capitalize_list_items(original_list):
    capitalized_list = []
    for item in original_list:
        capitalized_list.append(item.capitalize())
    return capitalized_list

fruits = ['banana', 'orange', 'apple', 'lemon']
print(f'{capitalize_list_items(fruits)}\n')

# QUESTION 11
print('QUESTION 11')
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]

def add_item(target_list, item_to_add):
    # 1. Add the item to the specific list passed in
    target_list.append(item_to_add)
    
    # 2. Return both lists as a tuple
    return food_stuff, numbers

# Now, when you call it, you get both back
updated_food, updated_nums = add_item(food_stuff, 'Meat')
print(f"Food: {updated_food}")
add_item(numbers, 5)
print(f"Numbers: {updated_nums}\n")

# QUESTION 12
print('QUESTION 12')
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]

def remove_item(target_list, item_to_remove):
    target_list.remove(item_to_remove)

    return food_stuff, numbers

removed_food, removed_nums = remove_item(food_stuff, 'Mango')
print(f'Food: {removed_food}')
remove_item(numbers,3)
print(f'Numbers: {removed_nums}\n')

# QUESTION 13
def sum_of_numbers(n):
    total = 0
    # range(1, 6) will give us 1, 2, 3, 4, 5
    for i in range(1, n + 1):
        total += i
    return total

print(sum_of_numbers(5))   # Output: 15
print(sum_of_numbers(10))  # Output: 55
print(sum_of_numbers(100)) # Output: 5050
print('\n')

# QUESTION 14
print('QUESTION 14')
def sum_of_odds(n):
    total = 0
    for i in range(1, n + 1, 2):
        total += i
    return total

print(sum_of_odds(5))
print('\n')

# QUESTION 15
print('QUESTION 15')
def sum_of_even(n):
    total = 0
    for i in range(2, n + 1, 2):
        total += i
    return total

print(sum_of_even(5))