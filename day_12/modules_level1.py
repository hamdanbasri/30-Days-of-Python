# DAY 12 - MODULES EXERCISES LEVEL 1

# QUESTION 1
import random
import string

def random_user_id():
    # Define the pool of characters: lowercase letters and digits
    characters = string.ascii_lowercase + string.digits
    
    # Generate 6 random choices from that pool and join them into a string
    user_id = ''.join(random.choices(characters, k=6))
    
    return user_id

print(random_user_id())

# QUESTION 2
print ('\nQUESTION 2')

def user_id_gen_by_user():
    amount_of_characters = int(input('Input amount of characters: '))
    amount_of_ID = int(input('How many ID do you want to generate? '))

    for number in range(amount_of_ID):
        characters = string.ascii_lowercase + string.digits    
        user_id = ''.join(random.choices(characters, k=amount_of_characters))
        print(user_id)
    return user_id

user_id_gen_by_user()

# QUESTION 3
print ('\nQUESTION 3')
from random import randint

# Generate three random integers
r = randint(0, 255)
g = randint(0, 255)
b = randint(0, 255)

# Convert them to strings and join them with commas
rgb_combined = ",".join([str(r), str(g), str(b)])

print('RGB(' + rgb_combined + ')')
