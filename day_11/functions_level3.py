# FUNCTIONS EXERCISE LEVEL 3

# QUESTION 1
def is_prime(number):
    # 1. Handle numbers less than 2
    if number < 2:
        return False
    
    # 2. Handle 2 and 3 specifically
    if number == 2 or number == 3:
        return True
    
    # 3. Exclude even numbers and multiples of 3
    if number % 2 == 0 or number % 3 == 0:
        return False

    # 4. Check from 5 upwards
    # We use (i * i <= number) as a substitute for the square root
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
            
    return True

# Testing
print(f'Is 17 a prime number? {is_prime(17)}')  # True
print(f'Is 100 a prime number? {is_prime(100)}\n') # False

# QUESTION 2
unique_list = ['Python', 'C#', 'C++', 'Javascript']

def is_unique(input_list):
    return len(set(input_list)) == len(input_list)

print(f'Is all the item in the list unique? {is_unique(unique_list)}\n')

# QUESTION 3
data_type_list = ['python', 100, 'Hamdan']
def is_same_data_type(data_list):
    # 1. Handle empty lists
    if not data_list:
        return True
        
    # 2. Get the type of the first element to use as a reference
    first_type = type(data_list[0])
    
    # 3. Check every item against that first type
    for item in data_list:
        if type(item) != first_type:
            print('Not all the data types are the same.\n')
            return False
            
    print('All the data is the same data type.\n')
    return True

is_same_data_type(data_type_list)

# QUESTION 4
def is_valid_variable(name):
    # 1. Check if it's actually a string
    if not isinstance(name, str):
        return False
    
    # 2. Check if it follows the naming rules (letters, numbers, underscores)
    if not name.isidentifier():
        return False
    
    # 3. Check against reserved keywords
    # Since you want no imports, here are the most common ones:
    keywords = {
        'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 
        'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
        'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 
        'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 
        'try', 'while', 'with', 'yield'
    }
    
    if name in keywords:
        return False
        
    return True

# Testing
print(is_valid_variable("my_var_1"))  # True
print(is_valid_variable("1st_value"))  # False (Starts with a number)
print(is_valid_variable("class"))      # False (Reserved keyword)
print(is_valid_variable("user-name"))  # False (Contains a hyphen)
print('\n')

# QUESTION 5

from countries_data import countries
def most_spoken_languages(countries_data, limit=10):
    counts = {}
    
    # Iterate through each country dictionary
    for country in countries_data:
        # Loop through the list of languages in that country
        for lang in country['languages']:
            counts[lang] = counts.get(lang, 0) + 1
    
    # Convert to a list of tuples and sort by the count (descending)
    # We sort by x[1] which is the count
    sorted_langs = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    
    # Return only the requested amount
    return sorted_langs[:limit]

def most_populated_countries(countries_data, limit=10):
    # Sort the list of dictionaries by the 'population' key
    sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
    
    # Clean up the output to only show name and population
    result = []
    for country in sorted_countries[:limit]:
        result.append({
            'country': country['name'],
            'population': country['population']
        })
        
    return result

top_ten_langs = most_spoken_languages(countries, 10)
top_ten_pop = most_populated_countries(countries, 10)

print(f'The top ten languages are: {top_ten_langs}\n')
print(f'The top ten population are: {top_ten_pop}\n')