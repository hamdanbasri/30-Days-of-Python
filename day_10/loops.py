# DAY 10

# EXERSICE LEVEL 1
# QUESTION 1
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('####  This is using for loop  ####')
for number in numbers:
    print(number)


print('####   This is using while loop   ####')
count = 0
while count < 11:
    print(count)
    count += 1

# QUESTION 2
print('####  This is using for loop reversed ####')
for reversed_number in range(10, 0, -1):
    print(reversed_number)

count = 10
print('####   This is using while loop reversed   ####')
while count > 0:
    print(count)
    count -= 1

# QUESTION 3 - INCOMPLETE
rows = 7
columns = 7
for row in range(rows):
    print('#')


# QUESTION 4
for row in range(rows):
    for col in range(columns):
        print('# ', end='')
    print()

# QUESTION 5
value = 0

while value < 11:
    print(f'{value} x {value} = {value * value}')
    value += 1

# QUESTION 6
language = ['Python', 'Numpy','Pandas','Django', 'Flask']
for lang in language:
    print(lang)

# QUESTION 7
for output_number in range(100):
    if((output_number % 2) == 0):
        print(output_number)

# QUESTION 8
for output_odd_number in range(99, 0, -2):
    print(output_odd_number)

# EXERSICE LEVEL 2
# QUESTION 1 - INCOMPLETE
for total_number in range(100):
    total_number += 1
    print(f'The sum of all numbers is {total_number}')
    # how do i calculate all the numbers?

# QUESTION 2
for even_number in range(100):
    even_number += 1
    print(f'The sum of all even numbers is {even_number}')
    print(f'The sum of all odd numbers is: {even_number}') # need to replace this with odd numbers

# EXERCISE LEVEL 3
# QUESTION 1

# QUESTION 2

# QUESTION 3

