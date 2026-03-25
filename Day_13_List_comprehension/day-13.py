numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [n for n in numbers if n < 1]
print(negative_and_zero)

print()

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [n for r in list_of_lists for n in r]
print(flat)

print()

tpl = [(i, i ** 0, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)]
for t in tpl:
    print(t)

print()

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flat = [[n[0].upper(), n[0][0:3].upper(), n[1].upper()] for r in countries for n in r]
print(flat)

print()

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_dict = [{'country' : n[0].upper(), 'city' : n[1].upper()} for r in countries for n in r]
for c in countries_dict:
    print(c)

print()

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
str_names = [' '.join(n) for r in names for n in r]
print(str_names)

print()

slope = lambda x1, y1, x2, y2 : (y2 -y1) / (x2 - x1)
print(slope(2, 2, 6, 10))