# DAY 11 - FUNCTIONS

# EXERCISES LEVEL 1
## QUESTION 1
Declare a function add_two_numbers. It takes two parameters and it returns a sum.

### SOLUTION
```python
print('QUESTION 1')
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total
print(f'Adding two numbers: {add_two_numbers(1,2)}\n')
```

## QUESTION 2
Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

### SOLUTION
```python
print('QUESTION 2')
def area_of_circle(radius):
    area = 3.14 * radius * radius
    return area
print(f'Area of Circle: {area_of_circle(40)}\n')
```

## QUESTION 3
Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

### SOLUTION
```python
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
```

## QUESTION 4
Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

### SOLUTION
```python
print('QUESTION 4')
celcius = 0
def convert_celcius_to_fahrenheit(celcius):
    fahrenheit = (celcius * (9/5)) + 32
    return fahrenheit

user_input = input("What is the temperature in °C? ")
celcius_val = float(user_input)

print(f'{celcius_val}°C to Fahrenheit (°F) is: {convert_celcius_to_fahrenheit(celcius_val)}°F\n')

```

## QUESTION 5
Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

### SOLUTION
```python
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
```

## QUESTION 6
Write a function called calculate_slope which return the slope of a linear equation

### SOLUTION
```python
print('QUESTION 6')
slope_output = 0
def calculate_slope(x1, x2, y1, y2):
    slope = (y2 - y1) / (x2 - x1)
    slope_output = slope
    return slope

print(f'The slope is valued at: {calculate_slope(20,2,33,4)}\n')
```

## QUESTION 7
Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

### SOLUTION
```python
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
```

## QUESTION 8
Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

### SOLUTION
```python
print('QUESTION 8')

def print_list(my_list):
    for element in my_list:
        print(element)

tech_stack = ['Python', 'JavaScript', 'SQL', 'HTML']
print(f'{print_list(tech_stack)}\n')
```

## QUESTION 9
Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
```
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"])) 
# ["C", "B", "A"]
```

### SOLUTION
```python
print('QUESTION 9')
def reverse_list(*numbers):
    num_list = list(numbers)
    num_list.reverse()
    return num_list

print(reverse_list(1, 2, 3, 4, 5))
print(f'{reverse_list("A", "B", "C")}\n') 
```
## QUESTION 10
Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

### SOLUTION
```python
print('QUESTION 10')
def capitalize_list_items(original_list):
    capitalized_list = []
    for item in original_list:
        capitalized_list.append(item.capitalize())
    return capitalized_list

fruits = ['banana', 'orange', 'apple', 'lemon']
print(f'{capitalize_list_items(fruits)}\n')
```
## QUESTION 11
Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
```
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]
```

### THOUGHT PROCESS
```
Question 11 is odd by itself, as I am not sure if the challenge is to print out both of the output. 

Because of this uncertainty, I decided to print both just as how the question is structured.
Since the questions wants to print 2 different Keys and Values, I am facing this weird unsure approach for 2 returns. 

2 returns doesnt make sense as once the code reads the first return it will exit the function. So if you can see the return is returning both lists as tuples. 

Then when I am calling out add_item, I have to call again add_item the second time in order for the output to print out as intended.
```

### SOLUTION
```python
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
```
## QUESTION 12
Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
```
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
```

### THOUGHT PROCESS
```
Question 12 becomes easy once Question 11 is solved. 

The only difference is instead of appending the value in the list, I just remove the value from the list instead. 

Then the weird return statement is rewritten since it works.
```

### SOLUTION
```python
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
```

## QUESTION 13 - SOLVED WITH GEMINI
Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
```
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
```

### THOUGHT PROCESS
```
My initial tought on going through Question 13. When looking at the output, how does sum_of_numbers(5) becomes 15? Is it multiply by 3?

Then there is sum_of_number(10) and the output is 55.

Nothing is making sense right now.

I had to ask Gemini on this, and it clears up a lot.
Apparently it is not any sort of multiplication, instead its a sum of numbers all together. So sum_of_numbers(5) actually means

1 + 2 + 3 + 4 + 5 = 15

Then there is sum_of_numbers(10):

1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
```

### SOLUTION
```python
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
```
## QUESTION 14
Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

### THOUGHT PROCESS
```
So when approaching this, I need to modify question 13 slightly.

Lets say I am calling sum_of_odds(5)

I need it to calculate:

1 + 3 + 5 = 9.
```

### SOLUTION
```
Well this is when I found the usefulness of **STEP** when using range.

Comparing Question 13 and Question 14.

I simply have to set the for loop to account the step as below:

for i in range(1, n + 1, 2):

This will start the count at 1 and skip every other number, giving me only the odd numbers: 1, 3, 5, 7, 9.
```

```python
def sum_of_odds(n):
    total = 0
    for i in range(1, n + 1, 2):
        total += i
    return total

print(sum_of_odds(5))
print('\n')
```
## QUESTION 15
Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

### THOUGHT PROCESS
``` 
I might be able to use step again for this one, instead of step 2, I will try with step 1.

If I call sum_of_even(5) now it should be:

2 + 4 = 6
```

### SOLUTION
```
I was wrong about changing the step to 1, as that only makes the count increment by 1, not what I was thinking and I understood step wrongly. 
Gemini explained that it was as simple as changing the start number inside the range to 2. 
And then the total instead of adding 1, add the number of i for each loop. That makes sense.
```

```python
print('QUESTION 15')
def sum_of_even(n):
    total = 0
    for i in range(2, n + 1, 2):
        total += i
    return total

print(sum_of_even(5))
```


# EXERCISES LEVEL 2
## QUESTION 1
Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
```
print(evens_and_odds(100))
# The number of odds are 50.
# The number of evens are 51.
```

### THOUGHT PROCESS
```
1. I have to make sure the parameter only takes in a positive integer.
2. Find the remainder of the parameter with % 2.
3. If remainder is == 0 its an even number, else it is a negative.
4. Identify the even number by putting them into two separate lists.
5. Count the length of the list.
```
### SOLUTION
```
I was almost there, but again I was stuck because of the two return statement. Eventhough I was so close for getting only the even number I needed the help of Gemini. I need to understand further why am I returning it as a tuple.
```

```python
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
print(f'The number of odds are: {len(all_odds)}')
```
## QUESTION 2
Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

### THOUGHT PROCESS
```
I have no idea what factorial is until I google it.
The Factorial of a whole number 'n' is defined as the product of that number with every whole number less than or equal to 'n' till 1. For example, the factorial of 4 is 4 × 3 × 2 × 1, which is equal to 24. It is represented using the symbol '!'

e.g., 5! = 5 x 4 x 3 x 2 x 1 = 120
```
#SOLUTION
```python
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
print(f'The factorial of the whole number is {factorial(6)}\n')
```

## QUESTION 3
Call your function is_empty, it takes a parameter and it checks if it is empty or not

### THOUGHT PROCESS
```
The question is clear, but now at the back of my head is to compare if user_value != null. Now my question before I do this is, does python has a != null? Or != ''
```
### SOLUTION
```
To answer my own question, I discovered that in Python you can compare an empty value to None. However it was not showing it as empty as even when the user presses enter Python inteprates is as having a value of "". Gemini helps by telling me that in order to make sure that the value is empty, I can either just use not user_value or comparing the len(user_value) == 0. That makes a lot of sense. Also Gemini mentions that there might be a case where a user just inputs a spacebar, to avoid any unwanted output. It was recommended to strip the input so that it ignores spaces.
```
```python
print('QUESTION 3')
user_value = input('Please input a value: ').strip()
def is_empty(user_value):
    if not user_value:
        print('No value')
    else:
        print(f'The user inputs: {user_value}')
    return user_value
is_empty(user_value)
```

## QUESTION 4
Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

### THOUGHT PROCESS
```
In order to start I need to create a list_of_numbers = ['1','2','3','4','5']. 

Now to be honest, I have no idea how to calculate any of this. So for my attempt, lets just go through the old ways of googling and stack overflow before asking Gemini to help with each functions.

So below are my Google findings:

MEAN
To calculate the mean (average), add all the numbers in your data set together to find the sum, then divide that sum by the total count of numbers.
Sum: 2 + 2 + 4 + 6 + 8 + 10 = 32

MEDIAN
To find the median, first order your data from lowest to highest. If there is an odd number of values, the median is the middle number. If there is an even number of values, the median is the average of the two middle numbers (sum them and divide by two)

MODE
The mode is the value that appears most frequently in a data set. To calculate it, list the data points, count the frequency of each, and identify the highest count. A data set can have one mode, multiple modes (bimodal/multimodal), or no mode if all numbers appear equally.

RANGE
The range in statistics is calculated by finding the difference between the highest (H) and lowest (L) values in a data set. Simply order the data, identify the maximum and minimum, and use the formula: Range = Highest Value - Lowest Value. It measures the spread of data but is highly sensitive to outliers.

VARIANCE
Variance measures data spread around the mean. Calculate it by finding the mean, subtracting the mean from each data point, squaring those differences, summing them, and dividing by the count of numbers (n) for a population, or n-1 for a sample.

STD
To calculate standard deviation, find the mean of the data, subtract the mean from each number and square the results, average these squared differences (divide by n-1 for sample, 
N for population), and take the square root. A low standard deviation means data is close to the mean; a high one means it is spread out.
```

### SOLUTION
```
This is hard, I have not been into this sort of mathematical calculation since my Diploma. 
It is a good refresher, maybe I should do more of this kind of mathematical problems to solve.
```
```
Refer to functions_level2.py for the solutions.
```

## QUESTION 5
Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.
```
greet()
# "Hello, Guest!
greet("Alice")
# "Hello, Alice!"
```

### THOUGHT PROCESS
```
This sounds striaght forward, lets see if I can do this without any external help.
```
### SOLUTION
```
Just as I thought, it's the same approach as Question 3. Solved.
```
```python
print('QUESTION 5')
name = input('What is your name? ').strip()
def greet(name):
    if not name:
        print('Hello, Guest!')
    else:
        print(f'Hello, {name}')
    return name
greet(name)
```
## QUESTION 6
Create a function called show_args to take an arbitrary number of named arguments and print their names and values.
```
show_args(name="Alice", age=30, city="New York")
# Received: name: Alice, age: 30, city: New York
show_args(name="Bob", pet="Fluffy, the bunny")
# Received: name: Bob, pet: Fluffy, the bunny
```

### THOUGHT PROCESS
```
Arbritrary number of named arguments? What?
Okay I found some example in the readme for Day 11 which is useful.
So here is my solution.
```

### SOLUTION
```python
dict_1 = {"name":"Alice", "age":30, "city":"New York"}
dict_2 = {"name":"Bob", "pet":"Fluffy, the bunny"}
print('QUESTION 6')
def show_args(**args):
    for k, v in args.items():
        print("Received:", k,":", v)
show_args(**dict_1)
show_args(**dict_2)
```
# EXERCISES LEVEL 3
## QUESTION 1
Write a function called is_prime, which checks if a number is prime.

## QUESTION 2
Write a functions which checks if all items are unique in the list.

## QUESTION 3
Write a function which checks if all the items of the list are of the same data type.

## QUESTION 4
Write a function which check if provided variable is a valid python variable

## QUESTION 5
Go to the data folder and access the countries-data.py file.
* Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
* Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.