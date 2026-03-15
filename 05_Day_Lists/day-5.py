countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];

lst = list()

fruit = ['apple', 'peach', 'mango', 'banana', 'strawberry', 'cherry', 'pear']

print(len(fruit))

print()

print(fruit[0], fruit[3], fruit[6])

print()

mixed_data_types = ['Dom', 150, 5.10, 'Married', '123 New York']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)

print()

print('Number of companies:', len(it_companies))

print()

print('first, middle, and last company:', it_companies[0], it_companies[3], it_companies[6])

print()

it_companies[5] = 'Netflix'
print(it_companies)

print()

it_companies.append('Tesla')

print()

print(it_companies)

print()

it_companies.insert(4, 'Sony')
print(it_companies)

print()

it_companies[6] = it_companies[6].upper()
print(it_companies)

print()

str_it_companies = '#; '.join(it_companies)
print(str_it_companies)

print()

print('is Apple in the list?', 'Apple' in it_companies)

print()

it_companies.sort()
print('sorted IT companies', it_companies)

print()

it_companies.reverse()
print('reversed IT companies in descending order', it_companies)

print()

print('first 3 companies:', it_companies[0:3])

print()

print('last 3 companies:', it_companies[-3:])

print()

print('middle IT company:', it_companies[4])

print()

print('last IT company:', it_companies.pop())

print()

it_companies.clear()
print('remove all IT companies:', it_companies)

print()

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print('join the 2 lists:', front_end)

print()

full_stack = front_end.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print('full stack after adding Python and SQL', full_stack)

print()

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min = ages[0]
max = ages[-1]
print('min and max age:', min, ',', max)

print()

ages.append(19)
ages.append(26)
print('median age:', (ages[5] + ages[6]) / 2)

print()

total_ages = ages[0] + ages[1] + ages[2] + ages[3] + ages[4] + ages[5] + ages[6] + ages[7] + ages[8] + ages[9] + ages[10] + ages[11]
average = total_ages / len(ages)
print('average age:', average)

print()

print('range of ages:', ages[-1] - ages[0])

print()

print('Compare the value of (min - average) and (max - average), use abs() method', abs(min - average), ',', abs(max - average))

print()

print('tot lenght of countries', len(countries))

print()
 
print('middle country:', countries[97])

middle = (len(countries) + 1) // 2
first_half = countries[:middle]
second_half = countries[middle:]

print()

other_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, scandic = other_countries[0], other_countries[1], other_countries[2], other_countries[3:]
print('first three countries', china, russia, usa)

print()

print('scandic:', scandic)
