# DAY 6
# EXERCISE LEVEL 1

# QUESTION 1
tpl = ()

# QUESTION 2
sibling = ('jon', 'jean', 'kean', 'kurt')

# QUESTION 3
brothers = ('jon', 'kurt')
sisters = ('jean', 'kean')
siblings = brothers + sisters
print(siblings)

# QUESTION 4
print(f'Amount of siblings: {len(siblings)}')

# QUESTION 5
additional_families = ('father', 'mother')
family_members = siblings + additional_families
print (family_members)

# EXERCISE LEVEL 2
# QUESTION 1
print(f'Siblings: {family_members[0:4]}')
# print(f'Parents: {family_members[len(family_members)]}')

# QUESTION 2
fruits = ('apple', 'orange')
vegetables = ('cabbage', 'carrot')
animal_products = ('beef', 'chicken')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# QUESTION 3
food_stuff_tp_list = list(food_stuff_tp)
print(food_stuff_tp_list)

# QUESTION 4
print(len(food_stuff_tp)//2)
middle_of_list = int(len(food_stuff_tp)//2)
food_stuff_tp_list.pop(int(len(food_stuff_tp)//2))
print(food_stuff_tp_list)

# QUESTION 5
print(food_stuff_tp_list[0:3])
print(food_stuff_tp_list[len(food_stuff_tp_list)-1:-3])

# QUESTION 6
del food_stuff_tp

# QUESTION 7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)