from countries_data import countries
old_countries = [
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
]

num = 0
while num <= 10:
    print(num)
    num += 1

print()

for num in range(11):
    print(num)

print()

num = 10

while num >= 0:
    print(num)
    num -= 1

for num in range(10, -1, -1):
    print(num)

print()

for i in range(1, 8):
    print('#' * i)

print()

for i in range(8):
    for j in range(8):
        print('# ', end= ' ')
    print()

print()

num = 0

for i in range(11):
    print(f'{num} x {num} = {num * num}')
    num += 1

print()

lang_lst = ['Python', 'Numpy','Pandas','Django', 'Flask']

for item in lang_lst:
    print(item)

print()

for num in range(0,101,2):
    print(num)

print()

for num in range(100):
    if num % 2 == 1:
        print(num) 

print()

num = 0

for i in range(101):
    num += i
print('The sum of all numbers is', num)

print()

even = 0
odd = 0

for i in range(101):
    if i % 2 == 0:
        even += i
    else:
        odd += i
print(f'The sum of all  evens is {even}. And the sum of all odds is {odd}.')

print()

for country in old_countries:
    if 'land' in country:
        print(country)

print()

fruit_list = ['banana', 'orange', 'mango', 'lemon']

for i in range(len(fruit_list) - 1, -1, -1):
    print(fruit_list[i])

print()

languages = 0

for country in countries:
    languages += len(country['languages'])
print('Total number of languages:', languages)

print()

languages = dict()

for country in countries:
    for lan in country['languages']:
        if lan not in languages:
            languages[lan] = 1
        else:
            languages[lan] += 1

sorted_languages = sorted(
    languages.items(),
    key=lambda item: item[1],
    reverse=True)

top_10 = sorted_languages[:10]

for language, count in top_10:
    print(f'{language}: {count}')

print()

most_populated = dict()

for country in countries:
    most_populated[country['name']] = country['population']

sorted_most_populated = sorted(
    most_populated.items(),
    key=lambda item: item[1],
    reverse=True)

top_10 = sorted_most_populated[:10]

for country, count in top_10:
    print(f'{country}: {count}')