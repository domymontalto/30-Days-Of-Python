import math

age = 33
height = 5.10
complex_num = 3 + 5j

base = int(input('Enter base: '))
height = int(input('Enter height: '))
print('The area of the triangle is', int(0.5 * base * height))

print()

side_a = int(input('Enter side a: '))
side_b = int(input('Enter side b: '))
side_c = int(input('Enter side c: '))
print('The perimeter of the triangle is', side_a + side_b + side_c)

print()

lenght = int(input('Enter lenght: '))
width = int(input('Enter width: '))
print('The area of the rectangle is', lenght * width)

print()

print('The perimeter of the rectangle is', 2 * (lenght + width))

print()

radius = int(input('Enter radius: '))
print('The area of the circle is', math.pi * radius * radius)

print()

print('The circunference of the circle is', 2 * math.pi * radius)

print()

#answer is -3
x = int(input('Input x to find for what value y becames 0: '))
print('Calculate the y: ', x ** 2 + 6 * x + 9)

print()

slope = 2
print('Slope:', slope)

print()

x = 0
y = 2 * x - 2
print('Y-intercept:', (x, y))

print()

x = 2 / 2
y = 0
print('X-intercept:', (x, y))

print()

x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
print('Slope is:', slope)

print()

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print('Distance:', distance)

print()

isFalse = len('python') != len('dragon')
print('len(python) != len(dragon)?', isFalse)

print()

is_in_both = 'on' in 'python' and 'on' in 'dragon'
print('is "on" both in python and dragon?',is_in_both)

print()

is_in_sentence = 'jargon' in 'I hope this course is not full of jargon.'
print('is jargon in sentence "I hope this course is not full of jargon?"', is_in_sentence)

print()

print('make this false "is "on" both in python and dragon?"',not is_in_both)

print()

print('lenght of python word in string', str(float(len('python'))))

print()

print('To evaluate if a number is even in python we do number % 2 == 0', 4 % 2 == 0)

print()

print('is he floor division of 7 by 3 equal to the int converted value of 2.7', 7 // 3 == int(2.7))

print()

print('is type of "10" equal to type of 10?', type('10') == type(10))

print()

print('is int("9.8") is equal to 10?', int(9.8) == 10)

print()

hours = int(input('Enter hours: '))
rate = int(input('Enter rate: '))
print('Your weekly earning is', hours * rate)

print()

years = int(input('Enter number of years you have lived: '))
print('You have lived for ' + str(60*60*24*365 * years) + ' seconds.')

print() 

first_num = 1
second_num = 2
third_num = 3
forth_num = 4
fifth_num = 5
print(first_num, first_num ** 0, first_num ** 1, first_num ** 2, first_num ** 3)
print(second_num, second_num ** 0, second_num ** 1, second_num ** 2, second_num ** 3)
print(third_num, third_num ** 0, third_num ** 1, third_num ** 2, third_num ** 3)
print(forth_num, forth_num ** 0, forth_num ** 1, forth_num ** 2, forth_num ** 3)
print(fifth_num, fifth_num ** 1, fifth_num ** 2, fifth_num ** 3)

