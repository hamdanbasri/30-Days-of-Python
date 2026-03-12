# FUNCTIONS EXERCISE LEVEL 2

# QUESTION 1
evens = []
odds = []

def find_numbers(limit):
    # Clear lists in case you run the function multiple times
    evens.clear()
    odds.clear()
    
    for i in range(limit + 1):
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    
    # Return both as a tuple
    return evens, odds

# Unpack the results into two separate variables
all_evens, all_odds = find_numbers(100)

print(f'The number of evens are: {len(all_evens)}')
print(f'The number of odds are: {len(all_odds)}')

