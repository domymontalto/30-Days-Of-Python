age = int(input('Enter your age:'))
if age >= 18:
    print('You are old enough to learn to drive.')
else:
    print(f'You need {18 - age} more years to learn to drive.')

print()

my_age = 25
your_age = int(input('Enter your age:'))
if my_age - your_age == 1:
    print('I am 1 year older than you.')
elif my_age > your_age:
    print(f'I am {my_age - your_age} years older than you.')
elif your_age - my_age == 1:
    print('You are 1 year older than me.') 
elif your_age > my_age:
    print(f'You are {your_age - my_age} years older than me.')
else:
    print('We have the same age.')

print()

num_one = int(input('Enter number one:'))
num_two = int(input('Enter number two:'))
if num_one > num_two:
    print('a is greater than b')
elif num_two > num_one:
    print('a is smaller than b')
else:
    print('a is equal to b')

print()

student_score = int(input('Enter your score:'))
if student_score >= 90:
    print('A')
elif student_score >= 80:
    print('B')
elif student_score >= 70:
    print('C')
elif student_score >= 60:
    print('D')
else:
    print('F')

print()

month = input('What month are we in? ')
if month == 'September' or month == 'October' or month == 'November':
    print("it's Autumn")
elif month == 'December' or month == 'January' or month == 'February':
    print("it's Winter")
elif month == 'March' or month == 'April' or month == 'May':
    print("it's Spring")
elif month == 'June' or month == 'July' or month == 'August':
    print("it's Summer")

print()

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter a fruit: ')
if fruit not in fruits:
    fruits.append(fruit)
    print(fruits)
else:
    print('Fruit already exist')

print()

person = {'first_name':'Dom', 
           'last_name':'Montalto',
            'Age':150,
            'Country':'USA',
            'is_married': True,
            'Skills':['Python', 'Node', 'MongoDB'],
            'address': {
        'street': 'State Streat',
        'zipcode': '0101'
    }}
if 'Skills' in person:
    print(person['Skills'][len(person['Skills']) // 2])

if 'Skills' in person:
    if 'JavaScript' in person['Skills'] and 'React' in person['Skills']:
        print('He is a front end developer')
    elif 'Node' in person['Skills'] and 'Python' in person['Skills'] and 'MongoDB' in person['Skills']:
        print('He is a backend developer')
    elif 'React' in person['Skills'] and 'Node' in person['Skills'] and 'MongoDB' in person['Skills']:
        print('He is a fullstack developer')
    else:
        print('unknown title')

    if 'Python' in person['Skills']:
        print(person['Skills'])

if person['is_married'] == True and person['Country'] == 'USA':
    print(f'{person['first_name']} {person['last_name']} lives in {person['Country']}. He is married.')