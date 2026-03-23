import math
from countries_data import countries

def add_two_numbers(num_one, num_two):
    return num_one + num_two

print(add_two_numbers(3 , 4))

print()

def area_of_circle(r):
    return math.pi * r ** 2

print(area_of_circle(3)) 

print()

def add_all_nums(*nums):
        tot = 0
        for num in nums:
            if not isinstance(num, int):
                  return 'Not all items were numbers'
            tot += num
        return tot
    
print(add_all_nums(1, 2, 3, 4))

print()

def convert_celsius_to_fahreinheit(degrees_celsius):
    return (degrees_celsius * 9/5) + 32

print(convert_celsius_to_fahreinheit(30))

print()

def check_season(month):
    if month.lower() == 'december' or month.lower() == 'january' or month.lower() == 'febuary':
        return 'Winter'
    elif month.lower() == 'march' or month.lower() == 'april' or month.lower() == 'may':
        return 'Spring'
    elif month.lower() == 'june' or month.lower() == 'july' or month.lower() == 'august':
        return 'Summer'
    elif month.lower() == 'september' or month.lower() == 'october' or month.lower() == 'november':
        return 'Fall'
    
print(check_season('september'))

print()
    
def calculate_slope(m, b):
    return m

print(calculate_slope(3, 6))

print()

def print_list(lst):
    for element in lst:
        print(element)

print_list([1, 2, 3, 4, 5])

print()

def reverse_list(lst):
    new_list = []
    for i in range(len(lst), 0, -1):
        new_list.append(lst[i - 1])
    return new_list

print(reverse_list([1, 2, 3, 4, 5]))

print()

def capitalize_list_items(lst):
    new_list = []
    for item in lst:
        new_list.append(item.title())
    return new_list

print(capitalize_list_items(['hi', 'hello']))

print()

def add_item(lst, num):
    new_list = []
    new_list.extend(lst)
    new_list.append(num)
    return new_list

print(add_item([1, 2 , 3], 4))

print()

def remove_item(lst, num):
    new_list = []
    new_list.extend(lst)
    new_list.remove(num)
    return new_list

print(remove_item([1, 2, 3, 4], 3))

print()

def sum_of_numbers(num):
    tot = 0
    for i in range(num + 1):
        tot += i
    return tot

print(sum_of_numbers(10))

print()

def sum_of_odds(num):
    tot = 0
    for i in range(num + 1):
        if i % 2 != 0:
            tot += i
    return tot

print(sum_of_odds(100))

print()

def sum_of_even(num):
    tot = 0
    for i in range(num + 1):
        if i % 2 == 0:
            tot += i
    return tot

print(sum_of_even(100))

print()

def evens_and_odds(num):
    evens = 0
    odds = 0
    for i in range(num + 1 ):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return f'The number of odds are {odds}.\nThe number of evens are {evens}.' 

print(evens_and_odds(100))

print()

def factorial(num):
    tot = 1
    for i in range(1, num + 1):
        tot *= i
    return tot

print(factorial(5))

print()

def is_empty(lst):
    if len(lst) < 1:
        return 'Empty'
    else:
        return 'Not empty'
    
print(is_empty([]))

print()

def greet(name = 'Guest'):
    print(f'Hello, {name}!')

greet()

print()

def show_args(**args):
    for key, value in args.items():
        print(f'{key}: {value}', end = ', ')

show_args(name="Dom", age=150, city="New York")

print()

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return 'Not prime'
    return 'Prime'

print(is_prime(7))

print()

def all_unique(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
        else:
            return 'Not all unique'
    return 'All unique'

print(all_unique([1, 2, 3, 3, 4]))

print()

def all_unique(lst):
    new_list = []
    new_list.append(type(lst[0]))
    for i in range(1, len(lst)):
        if type(lst[i]) not in new_list:
            return 'Not all unique types'
    return 'All unique types'

print(all_unique([1, 2, 3, '3', 4]))

print()

def most_spoken_languages():
    languages = dict()

    for country in countries:
        for lang in country['languages']:
            if lang not in languages:
                languages[lang] = 1
            else:
                languages[lang] += 1
    
    sorted_languages = sorted(languages.items(), key = lambda item : item[1], reverse= True)
    return sorted_languages[:10]

print(most_spoken_languages())

print()

def most_populated_countries():
    most_populated = dict()

    for country in countries:
        most_populated[country['name']] = country['population']

    sorted_most_populated = sorted(most_populated.items(), key = lambda item : item[1], reverse= True)
    return sorted_most_populated[:10]

print(most_populated_countries())


