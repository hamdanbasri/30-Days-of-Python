# Day 13 List Comprehension

## QUESTION 1
Filter only negative and zero in the list using list comprehension
```
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
```
### THOUGHT PROCESS
```
With the example provided in the Readme, I manage to figure out the solution.
```
### SOLUTION
```python
# QUESTION 1
print ('QUESTION 1')
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_zero_numbers = [i for i in numbers if i <= 0]
print(negative_zero_numbers) 
```

## QUESTION 2
Flatten the following list of lists of lists to a one dimensional list :
```
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

output
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```
### THOUGHT PROCESS
```
Same here, the solution is already provided in the Readme file. The only difference is the value in the two dimensional array.
```
### SOLUTION
```python
# QUESTION 2
print ('\nQUESTION 2')
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list) 
```

## QUESTION 3
Using list comprehension create the following list of tuples:
```
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
```
### THOUGHT PROCESS
```
This is a bit confusing, so I had to ask Gemini. In order for me to get the following number, I have to calculate the base number for each value within the range.
```
### SOLUTION
```python
# The logic: (base_number, i**0, i**1, i**2, i**3, i**4, i**5)
challenge_list = [tuple([i] + [i**j for j in range(6)]) for i in range(11)]

# Let's print it
for row in challenge_list:
    print(row)
```

## QUESTION 4
Flatten the following list to a new list:
```
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
```
### THOUGHT PROCESS
```
Hmm, my initial approach was not even close. This List comprehension is confusing. Does this mean that I can put the condition first? Only then the value? 
```
### SOLUTION
```python
# QUESTION 4
print ('\nQUESTION 4')
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_list = [
    [name.upper(), name[:3].upper(), city.upper()] 
    for sublist in countries 
    for name, city in sublist
]

print(flattened_list)
```

## QUESTION 5
Change the following list to a list of dictionaries:
```
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]
```
### THOUGHT PROCESS
```
Fully Gemini, I'm blurred out. Although I'm starting to understand it. Lets see how I do in the next question.
```
### SOLUTION
```python
# QUESTION 5
print ('\nQUESTION 5')
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# List comprehension creating dictionaries
countries_dict_list = [
    {'country': name.upper(), 'city': city.upper()} 
    for sublist in countries 
    for name, city in sublist
]
```

## QUESTION 6
Change the following list of lists to a list of concatenated strings:
```
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
```
### THOUGHT PROCESS
```
Well I was overconfident and was wrong again, I was confused on how to
flattened a List of Lists of Tuples. Gemini to the rescue
```
### SOLUTION
```python
# QUESTION 6
print ('\nQUESTION 6')
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [f"{first} {last}" for sublist in names for first, last in sublist]
print(full_names)
```

## QUESTION 7
Write a lambda function which can solve a slope or y-intercept of linear functions.
### THOUGHT PROCESS
```
Again this is from Gemini, but lambda is easier to understand compared to List Comprehension.
After the keyword lambda I can just provide the parameters and then the execution.
Similar to C# approach. 
get_slope >= (y2 - y1) / (x2 - x1);
Example
x = lambda param1, param2, param3: param1 + param2 + param3
print(x(arg1, arg2, arg3))
```
### SOLUTION
```python
# QUESTION 7
print ('\nQUESTION 7')
get_slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

print(f"Slope: {get_slope(2, 4, 4, 10)}")
```