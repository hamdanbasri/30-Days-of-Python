# EXERCISE DAY 8 - DICTIONARIES

# QUESTION 1
dog = {}

# QUESTION 2
dog['name'] = 'Abu'
dog['color'] = 'Green'
dog['breed'] = 'Mutated'
dog['legs'] = 10
dog['age'] = 0.9

print(dog)

# QUESTION 3
student = {
    'first_name':'Hamdan', 
    'last_name':'Danny', 
    'Gender':'Alien', 
    'Age':1000, 
    'Marital Status':'Yes', 
    'Skill':['Folding Clothes', 'Lifting Aircrafts', 'Placing Cones'], 
    'Country':'Valhalla', 
    'City':'San Andreas'
    }

# QUESTION 4
print(f'Length of Student Dictionary: {len(student)}')

# QUESTION 5
values = student.get('Skill')
print(f'Skills of Student: {values}')

# QUESTION 6
student['Skill'].append('Dodging Bullets')
print(student)

# QUESTION 7
print(f'Student Dictionary Keys: {student.keys()}')

# QUESTION 8
print(f'Student Dictionary Values: {student.values()}')

# QUESTION 9
print(f'Dictionary to list of tuples: {student.items()}')

# QUESTION 10
student.pop('last_name')
print(student)

# QUESTION 11
del(student)