import math

concatenated = '{} {} {} {}'.format('Thirty', 'Days', 'Of', 'Python')
print(concatenated)

print()

coding = 'Coding'
for_ = 'For'
all = 'All'
concatenated = f'{coding} {for_} {all}'
print(concatenated)

print()

company = 'Coding For All'
print(company)

print()

print(len(company))

print()

print(company.upper())

print()

print(company.lower())

print()

print(company.capitalize())

print()

print(company.title())

print()

print(company.swapcase())

print()

print(company.strip('Coding'))

print()

print(company.find('Coding'))

print()

print(company.replace('Coding', 'Fan'))

print()

py_company = 'Python for Everyone'
print(py_company.replace('Everyone', 'All'))

print()

print(company.split())

print()

tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_companies.split(', '))

print()

print(company[0])

print()

print(company.rindex('l'))

print()

print(company[10])

print()

py_company_abr = py_company[0] + py_company[7] + py_company[11]
print(py_company_abr)

print()

company_abr = company[0] + company[7] + company[11]
print(company_abr)

print()

print(company.index('C'))

print()

print(company.index('F'))

print()

print(company.rindex('l'))

print()

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))

print()

print(sentence.rindex('because'))

print()

print(sentence[31:54])

print()

print(sentence.find('because'))

print()

print(company.startswith('Coding'))

print()

print(company.endswith('coding'))

print()

with_spaces = '   Coding For All      '
print(with_spaces[3:17])

print()

ident = 'thirty_days_of_python'
print(ident.isidentifier())

print()

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(libraries))

print()

print("I am enjoying this challenge.\nI just wonder what is next.")

print()

print("Name\tAge\tCountry\tCity")

print()

radius = 10
area = math.pi * radius ** 2
print('the area of a circle with radius {} is {:.2f} meters square'.format(radius, area))

print()

first_num = 8
second_num = 6
print('{} + {} = {}'.format(first_num, second_num, first_num + second_num))
print('{} - {} = {}'.format(first_num, second_num, first_num - second_num))
print('{} * {} = {}'.format(first_num, second_num, first_num * second_num))
print('{} / {} = {:.2f}'.format(first_num, second_num, first_num / second_num))
print('{} % {} = {}'.format(first_num, second_num, first_num % second_num))
print('{} // {} = {}'.format(first_num, second_num, first_num // second_num))
print('{} ** {} = {}'.format(first_num, second_num, first_num ** second_num))