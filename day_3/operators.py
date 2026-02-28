# Day 3: 30 Days of python programming

# QUESTION 1,2,3
# age = 34
# height = 168.5
# complex_number = 0

# QUESTION 4
# print('Calculate the area of a triangle')
# base = input('Enter base amount: ')
# height = input('Enter height amount: ')

# base_float = float(base)
# height_float = float(height)

# print(f'The area of the triangle is {0.5 * base_float * height_float}' )

# QUESTION 5
# print('Get the perimeter of a triangle')
# a = input('Enter side a: ')
# b = input('Enter side b: ')
# c = input('Enter side c: ')

# a_int = int(a)
# b_int = int(b)
# c_int = int(c)

# perimter = (a_int + b_int + c_int)
# print(f'The perimeter of the triangle is {perimter}')

# QUESTION 6
# print('Calculate the area and perimeter of a rectangle by providing the length and width')
# length = input('Input Length: ')
# width = input('Input Width: ')

# length_float  = float(length)
# width_float = float(width)

# area = length_float * width_float
# perimeter = 2 * length_float * width_float
# print(f'The area of the rectangle is: {area}')
# print(f'The perimeter of a rectangle is: {perimeter}')

# QUESTION 7
# print('Get radius of a circle')
# radius = input('Specify radius: ')
# radius_float = float(radius)

# print(f'The area of a circle is: {3.14 * radius_float * radius_float}')
# print(f'The circumference of a circle is: {2 * 3.14 * radius_float}')

# QUESTION 8
# print('Calculate the slope of x-intercept and y-intercept')
# x_intercept = input('Specify x-intercept: ')
# x_intercept_float = float(x_intercept)
# y_intercept = (2 * x_intercept_float)-2
# print(f'The slope is: {y_intercept}')

# # QUESTION 9
# x1 = 2
# x2 = 6
# y1 = 2
# y2 = 10
# slope = (y2-y1)/(x2-x1)
# print(f'The euclidian distance is: {slope} ')

# # QUESTION 10
# if(y_intercept == slope):
#     print('The slope and euclidian angle are equals')
# else:
#     difference = y_intercept - slope
#     print(f'The slope and euclidian angles are not equals, the diffference is {difference}')

#  QUESTION 11 - UNSURE OF THE ANSWER
# print('Calculate the value of y (y = x^2 + 6x + 9)')
# x = input('Specify x value: ')
# x_float = float(x)
# y_temp = x_float**2
# y = y_temp * (y_temp + (6*x_float) + 9)
# print(f'The value of y is: {y}')

# QUESTION 12
# print(f'The length fo the word python is: {len('python')}')
# print(f'The length of the word dragon is: {len('dragon')}')
# print(len('python') != len('dragon'))

# QUESTION 13
# print('Does the word on exist in', 'on' in 'python' and 'dragon', 'on' in 'dragon')

# # QUESTION 14
# print('I hope this course is not full of jargon.', 'jargon' in 'I hope this course is not full of jargon.')

# QUESTION 15
# print('on is not in python and dragon: ', 'ON' in 'python' and 'ON' in 'dragon')

# QUESTION 16
# length_of_word = len('ptyhon')
# print(f'Word is: {length_of_word}')
# word_in_float = float(length_of_word)
# print(f'Length of word is: {word_in_float}')
# word_in_string = str(word_in_float)
# print(f'The word converted to string: {word_in_string}')

# QUESTION 17
# print('Check if the number is even or odd')
# is_number_even = input("Input Number: ")
# num_int = float(is_number_even)
# calculate = num_int % 2
# print('The division of 2 is', calculate)
# if(calculate == 0):
#     print('Number is even')
# else:
#     print('Number is odd')

# QUESTION 18
# floor_division = 7 // 3
# floor_int = int(2.7)
# print(floor_division)
# print(floor_int)
# print(floor_division == floor_int)

# QUESTION 19
# print(type('10') == type(10))

# QUESTION 20
# print(int(9.8) == 10)

# QUESTION 21
# hours = input('Enter hours: ')
# rate_per_hour = input('Enter rate per hour: ')
# print(f'Your weekly earning is: {float(hours) * float(rate_per_hour)}')

# QUESTION 22
# years = int(input('Enter number of years you have lived: '))
# seconds_in_one_year = 365 * 24 * 60 * 60
# total_seconds = years * seconds_in_one_year
# print(f'You have lived for {total_seconds} seconds.')

# QUESTION 23
for n in range(1, 6):
    print(n, n**0, n**1, n**2, n**3)