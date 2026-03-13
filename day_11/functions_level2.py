# FUNCTIONS EXERCISE LEVEL 2

# QUESTION 1
evens = []
odds = []

def find_numbers(limit):
    # Clear lists in case you run the function multiple times
    evens.clear()
    odds.clear()
    
    for i in range(limit + 1):
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    

    # Return both as a tuple
    return evens, odds

# Unpack the results into two separate variables
all_evens, all_odds = find_numbers(100)

print(f'The number of evens are: {len(all_evens)}')
print(f'The number of odds are: {len(all_odds)}\n')

# QUESTION 2
print('QUESTION 2')

def factorial(whole_number):
    if whole_number < 0:
        return "Factorial is not defined for negative numbers"
    elif whole_number == 0:
        return 1
    else:
        result = 1
        for i in range(1, whole_number + 1):
            result *= i
        return result
print(f'The factorial of the whole number is {factorial(5)}\n')

# QUESTION 3
print('QUESTION 3')
user_value = input('Please input a value: ').strip()
def is_empty(user_value):
    if not user_value:
        print('No value]n')
    else:
        print(f'The user inputs: {user_value}\n')
    return user_value
is_empty(user_value)

# QEUSTION 4
print('QUESTION 4')
list_of_numbers = ['5','2','7','2','8','1']
print(list_of_numbers)

def calculate_mean():
    mean = 0
    for number in list_of_numbers:
        mean = mean + int(number)
    print(f'The mean value of the list of numbers are: {mean}\n')
calculate_mean()

list_of_numbers = [10, 2, 38, 23, 3, 8] # Length is 6 (Even)

def calculate_median(nums):
    # 1. Sort the list
    sorted_list = sorted(nums)
    n = len(sorted_list)
    
    # 2. Find the middle index using floor division (//)
    mid = n // 2
    
    # 3. Check if even or odd
    if n % 2 == 0:
        # Get the two middle numbers
        # For length 6, indices are 2 and 3
        val1 = sorted_list[mid - 1]
        val2 = sorted_list[mid]
        median = (val1 + val2) / 2
    else:
        # If odd, just take the middle one
        median = sorted_list[mid]
        
    return median

result = calculate_median(list_of_numbers)
print(f'Sorted list: {sorted(list_of_numbers)}')
print(f'The median is: {result}\n')
    
def calculate_mode(numbers):
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    
    if not counts:
        return "List is empty, no mode."

    max_frequency = max(counts.values())
    
    # Check if all elements appear only once (no distinct mode)
    if max_frequency == 1 and len(set(numbers)) == len(numbers):
        return "No unique mode found; all elements appear once."

    # Find all elements with the maximum frequency
    modes = [key for key, value in counts.items() if value == max_frequency]
    return modes

print(f"The mode(s) are: {calculate_mode(list_of_numbers)}")
# def calculate_range():
# def calculate_variance():
# def calculate_std():


