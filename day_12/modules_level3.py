# DAY 12 - MODULES EXERCISES LEVEL 1

# QUESTION 1
print ('QUESTION 1')
item_list = [1,2,3,4]
import random
def shuffle_list(list_of_item):
    # k=len(...) tells Python to grab all items from the list in a random order
    shuffled = random.sample(list_of_item, k=len(list_of_item))
    return shuffled

# Testing it out
result = shuffle_list(item_list)
print(f"Original: {item_list}")
print(f"Shuffled: {result}")


# QUESTION 2
print ('\nQUESTION 2')
def generate_unique_numbers():
    # range(10) gives us numbers 0 through 9
    # k=7 tells Python we want exactly 7 of them
    numbers = random.sample(range(10), k=7)
    return numbers

# Testing the function
print(generate_unique_numbers())
