# DAY 4

# QUESTION 1 - CONCANTENATE THE WORDS
# word_one = 'thirty'
# word_two = 'days'
# word_three = 'of'
# word_four = 'python'
# combine = word_one + word_two + word_three + word_four
# print(combine)

# QUESTION 2 - CONCATENATE THE WORDS
# word_one = 'coding'
# word_two = 'for'
# word_three = 'all'
# combine = word_one + word_two + word_three
# print(combine)

# QUESTION 3
# company = 'Coding For All'

# QUESTION 4
# print(company)

# # QUESTION 5
# print(len(company))

# QUESTION 6 - TO UPPERCASE
# company = 'coding for all'
# print(company.swapcase())

# QUESTION 7 - TO LOWERCASE
# company = 'CODING FOR ALL'
# print(company.swapcase())

# QUESTION 8
# word = 'Coding For All'
# print(word.capitalize())
# print(word.title())
# print(word.swapcase())

# QUESTION 9 - SLICE
# word = 'Coding For All'
# first_word = word[0:6]
# print(first_word)

# QUESTION 10 - CHECK STRING CONTAIN WORD
# word = 'Coding For All'
# print(word.find('Coding'))

# # QUESTION 11 - REPLACE THE WORD
# word = 'Coding For All'
# print(word.replace('Coding', 'Python'))

# QUESTION 12 - REPLACE THE SENTENCE
# word = 'Python For Everyone'
# print(word.replace('Python For Everyone', 'Python For All'))

# QUESTION 13 - SPLIT
# word = 'Coding For All'
# print(word.split())

# QUESTION 14 - SPLIT THE STRING AT THE COMMA
# word = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
# print(word.split(', '))

# QUESTION 15 - IDENTIFY THE CHARACTER AT INDEX 0
# word = 'Coding For All'
# first_letter = word[0]
# print(first_letter)

# QUESTION 16 - IDENTIFY THE LAST CHARACTER
# word = 'Coding For All'
# last_letter = word[-1]
# print(last_letter)

# QUESTION 17
# word = 'Coding For All'
# letter = word[10]
# print(letter)

# QUESTION 18
# word = "Python For Everyone"

# acronym = ""
# for w in word.split():
#     acronym += w[0]

# print(acronym)

# QUESTION 19
# word = "Coding For All"

# acronym = ""
# for w in word.split():
#     acronym += w[0]

# print(acronym)

# QUESTION 20 - determine the position of the first occurrence of C
# word = 'Coding For All'
# sub_string = 'C'
# print(word.index(sub_string))

# # QUESTION 21 - determine the position of the first occurrence of F in Coding For All.
# word = 'Coding For All'
# sub_string = 'F'
# print(word.index(sub_string))

# # QUESTION 22 - determine the position of the last occurrence of l in Coding For All People.
# word = 'Coding For All People'
# print(word.rfind('l'))

# # QUESTION 23
# word = 'You cannot end a sentence with because because because is a conjunction'
# word_to_find = word.index('because')
# print(word_to_find)

# # QUESTION 24
# word = 'You cannot end a sentence with because because because is a conjunction'
# print(word.rfind('because'))

# # QUESTION 25 - slice
# word = 'You cannot end a sentence with because because because is a conjunction'
# print(word.replace('because', ''))

# # QUESTION 26
# word = 'You cannot end a sentence with because because because is a conjunction'
# print(word.find('because'))

# # QUESTION 27 - slice
# word = 'You cannot end a sentence with because because because is a conjunction'
# print(word.replace('because', ''))

# QUESTION 28
# word = 'Coding For All'
# print(word.startswith('Coding'))

# # QUESTION 29
# word = 'Coding For All'
# print(word.endswith('Coding'))

# # QUESTION 30
# word = '   Coding For All      '
# cleaned = word.strip()
# print(cleaned)

# # QUESTION 31
# word_one = '30DaysOfPython'
# word_two = 'thirty_days_of_python'
# print(word_one.isidentifier())
# print(word_two.isidentifier())

# QUESTION 32
# word = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
# result = '# '.join(word)
# print(result)

# # QUESTION 33
# word = 'I am enjoying this challenge.\nI just wonder what is next.'
# print(word)

# QUESTION 34
# word_one = ['Name','Age','Country','City']
# word_two = ['Basri', '250', 'KL', 'MY']
# result_one = '\t'.join(word_one)
# result_two = '\t'.join(word_two)
# print(result_one)
# print(result_two)

# QUESTION 35
# radius = 10
# print(f'radius = {radius}\narea = 3.14 * radius ** 2\nThe area of a circle with radius {radius} is {3.14 * radius ** 2} meters square')

# QUESTION 36
a = 8
b = 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
