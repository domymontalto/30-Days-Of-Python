dog = {}
dog['name'] = 'Rocky'
dog['color'] = 'Brown'
dog['legs'] = 2
dog['age'] = 7
print('Dog:', dog)

print()

student = {'first_name':'Dom', 
           'last_name':'Montalto',
            'Gender':'Male',
            'Age':150,
            'marital_status':'Married',
            'Skills':['Python', 'Swift', 'Java'],
            'Country':'USA',
            'City':'New York',
            'Address':'123 Main Streat'}
print('Lenght of student dictionary:', len(student))

print()

print('Type of value of student skills:', type(student['Skills']))

print()

student['Skills'].extend(['SQL', 'C#'])
print('Updated student skills:', student['Skills'])

print()

print('Student keys:', student.keys())

print()

print('Student values:', student.values())

print()

print('Student list:', student.items())

print()

del student['Address']
print('Student address deleted:', student)

print()

del student
