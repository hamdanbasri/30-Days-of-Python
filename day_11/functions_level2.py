# FUNCTIONS EXERCISE LEVEL 2

# QUESTION 1
even_list = []
odd_list = []
even_or_odd = 0

def evens_and_odds(random_number):
    if random_number > 0:
        while even_or_odd < random_number:
            even_or_odd += 1
            even_or_odd % 2
    # print(even_or_odd)

    if even_or_odd == 0:
        even_list.append(even_or_odd)
        print(even_list)
    else:
        odd_list.append(even_or_odd)
    return len(even_list)

print(f'The number of evens are: {len(even_list)}')
print(f'The number of odds are: {len(odd_list)}')
print(evens_and_odds(100))

