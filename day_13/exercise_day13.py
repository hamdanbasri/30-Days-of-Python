# DAY 13 - List Comprehension

# QUESTION 1
print ('QUESTION 1')
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_zero_numbers = [i for i in numbers if i <= 0]
print(negative_zero_numbers)   

# QUESTION 2
print ('\nQUESTION 2')
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list) 

# QUESTION 3
print('\nQUESTION 3')

# The logic: (base_number, i**0, i**1, i**2, i**3, i**4, i**5)
challenge_list = [tuple([i] + [i**j for j in range(6)]) for i in range(11)]

# Let's print it
for row in challenge_list:
    print(row)


# QUESTION 4
print ('\nQUESTION 4')
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_list = [
    [name.upper(), name[:3].upper(), city.upper()] 
    for sublist in countries 
    for name, city in sublist
]

print(flattened_list)

# QUESTION 5
print ('\nQUESTION 5')
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# List comprehension creating dictionaries
countries_dict_list = [
    {'country': name.upper(), 'city': city.upper()} 
    for sublist in countries 
    for name, city in sublist
]

print(countries_dict_list)

# QUESTION 6
print ('\nQUESTION 6')
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [f"{first} {last}" for sublist in names for first, last in sublist]
print(full_names)

# QUESTION 7
print ('\nQUESTION 7')
get_slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

print(f"Slope: {get_slope(2, 4, 4, 10)}")