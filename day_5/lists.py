# DAY 5

# EXERCISE LEVEL 1

# QUESTION 1
lst = []
print(lst)

# QUESTION 2
lst = ['laptop', 'television', 'console', 'smartphone', 'watch']

# QUESTION 3
print(len(lst))

# QUESTION 4
print(lst[0])
print(lst[2])
print(lst[4])

# QUESTION 5
mixed_data_types = ['hamdan', 34, 168, 'married', 'Kuala Lumpur']
print(mixed_data_types)

# QUESTION 6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# QUESTION 7
print(it_companies)

# QUESTION 8
print(len(it_companies))

# QUESTION 9
print(it_companies[0])
print(it_companies[2])
print(it_companies[-1])

# QUESTION 10
it_companies[0] = 'Meta'
print(it_companies)

# QUESTION 11
it_companies.append('oracle')
print(it_companies)

# QUESTION 12
it_companies.insert(4,'Alphabet')
print(it_companies)

# QUESTION 13
it_companies[0] = 'META'
print(it_companies)

# QUESTION 14
new_company = ['#;']
joined_company = it_companies + new_company
print(joined_company)

# QUESTION 15
does_exist = 'Alphabet' in it_companies
print(does_exist)

# QUESTION 16
it_companies.sort()
print(it_companies)

# QUESTION 17
# print(sorted(it_companies,reverse=True))

# # QUESTION 18
# print(it_companies[3:len(it_companies)])

# # QUESTION 19
# print(it_companies[0:len(it_companies)-3])

# QUESTION 20
count = (len(it_companies)//2)
print(count)
it_companies.remove(it_companies[count])
print(it_companies)

# QUESTION 21
it_companies.remove(it_companies[0])
print(it_companies)

# QUESTION 22
count = (len(it_companies)//2)
print(count)
it_companies.remove(it_companies[count])
print(it_companies)

# QUESTION 23
it_companies.remove(it_companies[len(it_companies)-1])
print(it_companies)

# QUESTION 24
it_companies.clear()
print(it_companies)

# QUESTION 25
# del it_companies
# print(it_companies)

# QUESTION 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(front_end + back_end)

# QUESTION 27
full_stack = front_end + back_end
new_stack = ['Python', 'SQL', 'Redux']
print(full_stack + new_stack)

# EXERCISE LEVEL 2

# QUESTION 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages.sort())
print(f'Min: {min(ages)}')
print(f'Max: {max(ages)}')
ages.append(min(ages))
ages.append(max(ages))
print(ages)
sorted_ages = sorted(ages)
print(sorted_ages)
n = len(sorted_ages)

if n % 2 == 0:
    median = (sorted_ages[n//2 - 1] + sorted_ages[n//2]) / 2
else:
    median = sorted_ages[n//2]

print("Median age:", median)
print(f'Average: {sum(ages)/2}')
print(f'Range: {max(ages) - min(ages)}')
print(f'Absolute Min: {abs(min(ages))}')
print(f'Absolute Maximum: {abs(max(ages))}')
print(f'Compare Absolute Maximum and Minimum: {abs(max(ages))-abs(min(ages))}')



# QUESTION 1_1

# QUESTION 2

# QUESTION 3

