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
```

### SOLUTION
```python
```

## QUESTION 2
Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
### THOUGHT PROCESS
```
```

### SOLUTION
```python
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
```

### SOLUTION
```python
```

# EXERCISE LEVEL 3
## QUESTION 1
Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
### THOUGHT PROCESS
```
```

### SOLUTION
```python
```

## QUESTION 2
Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
### THOUGHT PROCESS
```
```

### SOLUTION
```python
```