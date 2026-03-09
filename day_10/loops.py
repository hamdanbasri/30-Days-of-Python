# DAY 10

# EXERSICE LEVEL 1
# QUESTION 1
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print('####  This is using for loop  ####')
# for number in numbers:
#     print(number)


# print('####   This is using while loop   ####')
# count = 0
# while count < 11:
#     print(count)
#     count += 1

# QUESTION 2
# print('####  This is using for loop reversed ####')
# for reversed_number in range(10, 0, -1):
#     print(reversed_number)

# count = 10
# print('####   This is using while loop reversed   ####')
# while count > 0:
#     print(count)
#     count -= 1

# QUESTION 3
rows = 7
columns = 0

for row in range(rows):
    columns += 1
    print('#' * columns)

# total_countries = 0
# identified_countries = []
# for country in countries:
#     if country.find('land') > 0:
#         total_countries += 1
#         identified_countries.append(country.find('land'))
#         print(list(identified_countries))
#     # else:
#         # identified_countries = total_countries.strip(-1)
#         # print(countries[identified_countries])
# print(identified_countries)
# print(f"Total countries that has the word 'land': {total_countries}")


# QUESTION 4
rows = 8
columns = 8
for row in range(rows):
    for col in range(columns):
        print('# ', end='')
    print()

# QUESTION 5
# value = 0

# while value < 11:
#     print(f'{value} x {value} = {value * value}')
    # value += 1

# QUESTION 6
# language = ['Python', 'Numpy','Pandas','Django', 'Flask']
# for lang in language:
#     print(lang)

# QUESTION 7
# for output_number in range(100):
#     if((output_number % 2) == 0):
#         print(output_number)

# QUESTION 8
# for output_odd_number in range(99, 0, -2):
#     print(output_odd_number)

# EXERSICE LEVEL 2
# QUESTION 1
added_value = 0
for total_number in range(100):
        total_number += 1
        added_value += total_number
print(f'The sum of all numbers is {added_value}')

# QUESTION 2
even_number = 0
odd_number = 0
add_all_number = 0
for all_number in range(100):
    all_number += 1
    add_all_number += all_number
    if((all_number % 2) == 0):
        even_number += all_number
#print(add_all_number)
odd_number = add_all_number - even_number
#print(odd_number)      
print(f'The sum of all evens is {even_number}. And the sum of all odds is {odd_number}')

