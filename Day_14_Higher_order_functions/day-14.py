from functools import reduce
from countries import other_countries as others

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Map takes as parameters a funtion and an iterable and applies the fanction to each item
# Filter takes as parameters a funcion and an iterable and returns elements that are true
# Reduce takse as parameters a funcion and an iterable and returns iterable reduced to a single result

# Higher_order is a function that takes or returns another function
# Closure is a function that remembers variables where it was created
# Decorator is a function that add functionalities to another fanction

def square(x):
    return x ** 2

nums = [1, 2, 3]
result = map(square, nums)
print(list(result))

print()

def is_even(x):
    return x % 2 == 0

nums = [1, 2, 3, 4]
result = filter(is_even, nums)
print(list(result))

print()

def summation(x, y):
    return x + y

nums = [1, 2, 3]
result = reduce(summation, numbers)
print(result)

print()

for country in countries:
    print(country)

print()

for name in names:
    print(name)

print()

for number in numbers:
    print(number)

print()

def to_upper(word):
    return word.upper()

countries_upper = map(to_upper, countries)
print(list(countries_upper))

print()

def square(num):
    return num ** 2

numbers_squared = map(square, numbers)
print(list(numbers_squared))

print()

names_upper = map(to_upper, names)
print(list(names_upper))

print()

def has_land(country):
    if 'land' in country:
        return country

countries_land = filter(has_land, countries)
print(list(countries_land))

print()

def len_not_six(name):
    if len(name) != 6:
        return name

countries_not_len_six = filter(len_not_six, countries)
print(list(countries_not_len_six))

print()

def len_six_or_more(name):
    if len(name) >= 6:
        return name

countries_six_or_more = filter(len_six_or_more, countries)
print(list(countries_six_or_more))

print()

countries_without_e = filter(lambda x: 'e' not in x.lower(), countries)
print(list(countries_without_e))

print()

number_list = [1, 2, 3, 4, 5, 6,]
sum_of_even = reduce(lambda x, y : x + y, filter(lambda x : x % 2 == 0, number_list))

print(sum_of_even)

print()

mixed_types_list = ['hello', 1, 2, 3, 'hi', 'bye', 7]

get_string_lists = filter(lambda x : isinstance(x, str), mixed_types_list)
print(list(get_string_lists))

print()

summ = reduce(lambda x, y : x + y,  numbers)
print(summ)

print()

north_european_countries = reduce(lambda country, other_country: country + ', ' + other_country, countries[:len(countries) - 1]) + f', and {countries[-1]} are north European countries' 
print(north_european_countries)

print()

categorize_countries = filter(lambda country: 'island'.title() in country, others)
print(list(categorize_countries))

print()

letters = list(map(lambda c: c[0], countries))

def count_by_starting_letter():
    result = {}
    for letter in letters:
        result[letter] = result.get(letter, 0) + 1
    return result

print(count_by_starting_letter())

print()

def get_first_ten_countries():
    return others[:10]

print(get_first_ten_countries())

print()

def get_last_ten_countries():
    return others[-10:]

print(get_last_ten_countries())