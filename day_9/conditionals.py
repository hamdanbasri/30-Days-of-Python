# DAY 9 CONDITIONALS

# EXERCISE LEVEL 1
# QUESTION 1
# age = input('What is your age: ')
# age_diffrence = 18 - int(age)

# print('Output')
# if(age_diffrence < 0):
#     print('Valid age for driving license')
# else:
#     print(f'You need {age_diffrence} more years to learn to drive')

# QUESTION 2
# my_age = input('Enter your age: ')
# your_age = 30
# age_diff = your_age - int(my_age)

# if age_diff > 0:
#     print(f'You are {age_diff} years younger')
# elif age_diff < 0:
#     print(f'You are {int(my_age) - your_age} years older than me')
# else:
#     print('We are the same age')


# QUESTION 3
# a = input('Enter number one: ')
# b = input('Enter number two: ')

# if a > b:
#     print(f'{a} is greater than {b}')
# elif a < b:
#     print(f'{a} is smaller than {b}')
# else:
#     print(f'{a} is equal to {b}')

# EXERCISE LEVEL 2
# QUESTION 1
# score = 0
# if score >= 90 and score <= 100:
#     print('A')
# elif score >= 80 and score <= 89:
#     print('B')
# elif score >= 70 and score <= 79:
#     print('C')
# elif score >- 60 and score <= 69:
#     print('D')
# else:
#     print('F')

# QUESTION 2
# month = input('What month is it? ')
# if month == 'September' or month == 'Sep' or month == 'October' or month == 'Oct' or month == 'November' or month == 'Nov':
#     print('The season is Autumn')
# elif month == 'December' or month == 'Dec' or month == 'January' or month == 'Jan' or month == 'February' or month == 'Feb':
#     print('The season is Winter')
# elif month == 'March' or month == 'Mar' or month == 'April' or month == 'Apr' or month == 'May':
#     print('The season is Spring')
# else:
#     print('The season is Summer')


# QUESTION 3
# fruits = ['banana', 'orange', 'mango', 'lemon']

# fruit = input('What is your favorite fruit: ')
# does_exist = fruit in fruits
# if does_exist:
#     print('That fruit already exist in the list')
# else:
#     fruits.append(fruit)
#     print(fruits)

# EXERCISE LEVEL 3
# QUESTION 1
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

print('skills' in person)
print(f'The skills of this person is: {person.get('skills')}')
print(f'The middle skill is: {person['skills'][len(person.get('skills'))//2]}')
print(f'Does python exist in skills? {'Python' in person.get('skills')}')

if person.get('skill') == 'Javascript' and 'React':
    print('He is a front end developer')
elif person.get('skill') == 'Node' and 'Python' and 'MongoDB':
    print('He is a backend developer')
elif person.get('skill') == 'React' and 'Node' and 'MondoDB':
    print('He is a fullstack developer')
else:
    print('unknown title')

if person.get('is_married') and person.get('country') == 'Finland':
    print(f'{person.get('first_name')} {person.get('last_name')} lives in {person.get('country')}. He is married')