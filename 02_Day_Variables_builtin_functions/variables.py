#Day 2:30 Days of python programming
import math

first_name = 'Dom'
last_name = 'Montalto'
full_name = 'Dom Montalto'
country = 'USA'
city = 'New York'
age = '150'
year = '2026'
is_married = True
is_True = False
is_light_on = True
is_python, color = True, 'Green'

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_True))
print(type(is_light_on))
print(type(is_python))
print(type(color))

print(len(first_name))
print(len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

area_of_circle = math.pi * 30 ** 2
circum_of_circle = 2 * math.pi * 30
print(area_of_circle)
print(circum_of_circle)

radius = int(input("What is the radius? "))
print('area is: ', math.pi * radius ** 2)

first_name, last_name, country, age = input('name: '), input('last name: '), input('country: '), input('age: ')
print(first_name, last_name, country, age)

print(help('keywords'))