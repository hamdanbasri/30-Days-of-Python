# DAY 12 - MODULES EXERCISES LEVEL 2

# QUESTION 1
print ('QUESTION 1')
import random
import string
def list_of_hexa_colors():
    chars = "0123456789abcdef"    
    hexa_code = ''.join(random.choices(chars, k=6))    
    color = f'#{hexa_code}'
    print(color)
    return color

list_of_hexa_colors()

# QUESTION 2
print ('\nQUESTION 2')
from random import randint
def list_of_rgb_colors():
    rgb_Array = []
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb_combined = ",".join([str(r), str(g), str(b)])
    rgb_full = 'RGB(' + str(rgb_combined) + ')'
    rgb_Array.append(rgb_full)

    print(rgb_Array)

list_of_rgb_colors()

# QUESTION 3
print ('\nQUESTION 3')
color_choice = input("Do you want to generate RGB or Hexa colors (type 'rgb' or 'hexa') \n Answer: ")
color_amount = input("How many do you want to generate? (1-10) \n Answer:")
def generate_colors(type_of_color, amount_of_colors):
    if type_of_color == 'rgb':
        for numbers in range(int(amount_of_colors)):
            list_of_rgb_colors()
    elif type_of_color == 'hexa':
        for numbers in range(int(amount_of_colors)):
            list_of_hexa_colors()
    else:
        print("Please enter either 'rgb' or 'hexa'")

generate_colors('hexa', 3)
generate_colors('hexa', 1) 
generate_colors('rgb', 3)  
generate_colors('rgb', 1) 