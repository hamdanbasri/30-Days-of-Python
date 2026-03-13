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

list_of_numbers = ['5','2','7','2','8','1']
    
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

print(list_of_numbers)
print(f"The mode(s) are: {calculate_mode(list_of_numbers)}\n")

def calculate_range():
    sorted_list = sorted(list_of_numbers)
    print(sorted_list)
    high = sorted_list[len(sorted_list)-1]
    low = sorted_list[0]
    print(f'The highest value is: {high}')
    print(f'The lowest value is: {low}')
    print(f'The range between the highest and lowest is: {int(high) - int(low)}\n')
calculate_range()

def calculate_variance(nums):
    # 1. Convert strings to integers
    clean_nums = [int(x) for x in nums]
    n = len(clean_nums)
    
    # 2. Calculate the Mean (average)
    mean = sum(clean_nums) / n
    
    # 3. Calculate sum of squared differences
    # This is (x - mean)^2 for every number
    squared_diff_sum = sum((x - mean) ** 2 for x in clean_nums)
    
    # 4. Divide by n (Population Variance)
    variance = squared_diff_sum / n
    return variance

result = calculate_variance(list_of_numbers)
print(f"The variance is: {result:.2f}\n")


def calculate_std_dev(nums):
    # 1. Convert strings to integers
    clean_nums = [int(x) for x in nums]
    n = len(clean_nums)
    
    # 2. Calculate the Mean
    mean = sum(clean_nums) / n
    
    # 3. Calculate Variance
    squared_diff_sum = sum((x - mean) ** 2 for x in clean_nums)
    variance = squared_diff_sum / n
    
    # 4. Calculate Standard Deviation (Square root of variance)
    std_dev = variance ** 0.5
    return std_dev

result = calculate_std_dev(list_of_numbers)
print(f"The Standard Deviation is: {result:.2f}\n")

# QUESTION 5
print('QUESTION 5')
name = input('What is your name? ').strip()
def greet(name):
    if not name:
        print('Hello, Guest!')
    else:
        print(f'Hello, {name}\n')
    return name
greet(name)

# QUESTION 6
dict_1 = {"name":"Alice", "age":30, "city":"New York"}
dict_2 = {"name":"Bob", "pet":"Fluffy, the bunny"}
print('QUESTION 6')
def show_args(**args):
    for k, v in args.items():
        print("Received:", k,":", v)
show_args(**dict_1)
show_args(**dict_2)

