# Day 12 - MODULES

# EXERCISE LEVEL 1
## QUESTION 1
Write a function which generates a six digit/character random_user_id.
```
print(random_user_id()) 
  '1ee33d'
```

### THOUGHT PROCESS
```
Coming back to python after 5 days and concentrating on C# is making this a bit confusing. But I managed. I need to get used to the modules that is required to attempt each question.
Question 1 was done with the help of Gemini.
```

### SOLUTION
```python
import random
import string

def random_user_id():
    # Define the pool of characters: lowercase letters and digits
    characters = string.ascii_lowercase + string.digits
    
    # Generate 6 random choices from that pool and join them into a string
    user_id = ''.join(random.choices(characters, k=6))
    
    return user_id

print(random_user_id())

```
## QUESTION 2
Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
```
print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
   
print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr
```

### THOUGHT PROCESS
```
Proud to say that, for Questionn 2 after looking at the solution of Question 1. I have a better understanding and with a bit of scracthing of the head. I managed to solve it. Loops is all that is needed.
```

### SOLUTION
```python
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
```

## QUESTION 3
Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
```
print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form
```

### THOUGHT PROCESS
```
Hmm, almost like Question 1 & 2. Might need to find a random number between 0 and 255. And join them together.
```
```
What I did not consider was join only accepts strings, so I was stuck at joining the values. Gemini suggests that I split the random generation into 3 (R,G,B) then combine them while converting the int to string.
```
### SOLUTION
```python
print ('\nQUESTION 3')
from random import randint

# Generate three random integers
r = randint(0, 255)
g = randint(0, 255)
b = randint(0, 255)

# Convert them to strings and join them with commas
rgb_combined = ",".join([str(r), str(g), str(b)])

print('RGB(' + rgb_combined + ')')
```
# EXERCISE LEVEL 2
## QUESTION 1
Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
### THOUGHT PROCESS
```
My thought process tells me that I can modify Exercise 1 Level 2 to get the desired hexadecimal color output.
```
```
I was close with my own solution, however since I separated the numbers and letters, it shows up the numbers more. Gemini shows me the easy way to get the output.
```

### SOLUTION
```python
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
```

## QUESTION 2
Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
### THOUGHT PROCESS
```
This is quite straight forward, to test it, I put the condition to be in a for loop, which prints out 3 different RGB values in an Array.
```

### SOLUTION
```python
print ('\nQUESTION 2')
from random import randint
def list_of_rgb_colors():
    rgb_Array = []
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    for numbers in range(3):
        rgb_combined = ",".join([str(r), str(g), str(b)])
        rgb_full = 'RGB(' + str(rgb_combined) + ')'
        rgb_Array.append(rgb_full)

    print(rgb_Array)

list_of_rgb_colors()
```

## QUESTION 3
Write a function generate_colors which can generate any number of hexa or rgb colors.
```
generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
generate_colors('hexa', 1) # ['#b334ef']
generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
```
### THOUGHT PROCESS
```
Same here, I can just call the function in Question 1 and Question while having an if statement to check the selected color choice and asking the user how many colors they want to generate to pass into the parameter.
```

### SOLUTION
```python
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
```

# EXERCISE LEVEL 3
## QUESTION 1
Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
### THOUGHT PROCESS
```
Current thought process, just use import random. Then maybe randomized the number and add it into a new list.
```
```
Well almost there, but my logic doesnt truly shuffle the items. Now I know there is a random.sample which is really useful in this case.
```
```
### SOLUTION
```python
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
```

## QUESTION 2
Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
### THOUGHT PROCESS
```
Not much here, fully Gemini
```

### SOLUTION
```python
print ('\nQUESTION 2')
def generate_unique_numbers():
    # range(10) gives us numbers 0 through 9
    # k=7 tells Python we want exactly 7 of them
    numbers = random.sample(range(10), k=7)
    return numbers

# Testing the function
print(generate_unique_numbers())
```