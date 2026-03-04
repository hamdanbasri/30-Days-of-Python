# DAY 7 - SETS
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


# EXERCISE LEVEL 1
# QUESTION 1
print(len(it_companies))

# QUESTION 2
it_companies.add('Twitter')
print(it_companies)

# QUESTION 3
it_companies.update(['Threads', 'Capcut'])
print(it_companies)

# QUESTION 4
it_companies.remove('Twitter')
print(it_companies)

# QUESTION 5
# discard method wont raise any errors if the item from the set is not found

# EXERCISE LEVEL 2
# QUESTION 1
AB = A.union(B)
print(AB)

# QUESTION 2
print(f'Intersection between A & B {A.intersection(B)}')

# QUESTION 3
print(A.issubset(B))

# QUESTION 4
print(A.isdisjoint(B))

# QUESTION 5
print
BA = B.union(A)
print(BA)
ABBA = AB.union(BA)
print(f'ABBA: {ABBA}')

# QUESTION 6
print(f'Symmetric Difference: {A.symmetric_difference(B)}')

# QUESTION 7 - DELETE ALL THE SETS
del A
del B
del AB
del BA

# EXERCISE LEVEL 3
# QUESTION 1
age_set = set(age)
set_length = len(age_set)
list_length = len(age)

if(set_length > list_length):
    print(f'Set is longer: {set_length}, List is: {list_length}')
else:
    print(f'List is longer: {list_length}, Set is: {set_length}')

# QUESTION 2
print('Text is a string data type. Any data type written as text is a string.')
print('List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.')
print('A tuple is a collection of different data types which is ordered and unchangeable (immutable).')
print('Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed')

# QUESTION 3
sentence_1 = {'I', 'am', 'a', 'teacher', 'and'}
sentence_2 = {'I', 'love', 'to', 'inspire', 'and', 'teach', 'people'}
intersection = sentence_1.intersection(sentence_2)
print(f'Intersection: {intersection}')
joined_sentence = sentence_1.union(sentence_2)
print(f'Joined Sentence: {joined_sentence}')
joined_sentence.remove('I')
joined_sentence.remove('and')
print(f'Joined Sentence: {joined_sentence}')
print(f'The number of unique words is: {len(joined_sentence)}')