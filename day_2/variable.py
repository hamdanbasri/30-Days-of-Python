# Day 2: 30 Days of python programming

# Excercise Level 1
first_name = 'Hamdan'
last_name = 'Basri'
full_name = 'Hamdan Basri'
country = 'Malaysia'
city = 'Kuala Lumpur'
age = '34'
year = '2026'
is_married = True
is_true = True
is_light_on = False
console, workstation = 'ps5', 'lenovo'

# Excercise Level 1
# Q1
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(console))
print(type(workstation))
# Q2
print(len(first_name))

# Q3
first_name_len = len(first_name)
last_name_len = len(last_name)
print(f'Difference in length between first name and last is: {first_name_len - last_name_len} ')

# Q4
num_one = 5
num_two = 4

# Q5
total = num_one + num_two

# Q6
diff = num_two - num_one

# Q7
product = num_two * num_one

# Q8
division = num_one / num_two

# Q9
remainder = num_two % num_one

# Q10
exp = num_one ** num_two

# Q11
floor_division = num_one // num_two

# Q12

# A=πr2
area_of_circle = 3.14 * 30 ** 2
print(area_of_circle)

# C=2πr
circum_of_circle = 2 * 3.14 * 30
print(circum_of_circle)

radius = input('Specify the radius: ')
radius_int = int(radius)
user_area = 3.14 * radius_int ** 2
print(user_area)

# Q13
first_name = input('First Name: ')
last_name = input('Last Name: ')
country = input('Country: ')
age = input('Age: ')

print(first_name)
print(last_name)
print(country)
print(age)