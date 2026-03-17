tpl = tuple()
brothers = ('Mark', 'Tod', 'Dan')
sisters = ('Mary', 'Jade', 'Abbie')
siblings = brothers + sisters
print('Number of siblings:', len(siblings))

print()

parents = ('Tom', 'Kate')
family_members = parents + siblings
print(family_members)

print()

Father, Mother, Mark, Tod, Dan, Mary, Jade, Abbie = family_members

print(Father, Mother, Mark, Tod, Dan, Mary, Jade, Abbie)

print()

fruit = ('apple', 'banana', 'mango')
vegetables = ('cabage', 'carot', 'potato')
animals_products = ('fish', 'meat', 'eggs')
food_stuff_tp = fruit + vegetables + animals_products
print(food_stuff_tp)

print()

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

print()
middle = food_stuff_tp[4]
print(middle)

print()

first_three = food_stuff_lt[0:3]
last_three = food_stuff_lt[-3:]
print('First 3 food stuff:', first_three)
print('Last 3 food stuff:', last_three)

print()

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Is Estonia in nordic countries:', 'Estonia' in nordic_countries)
print('Is Iceland in nordic countries:', 'Iceland' in nordic_countries)