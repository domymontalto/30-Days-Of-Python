# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print('The lenght of it_companies is:', len(it_companies))

print()

it_companies.add('Twitter')
print('We added Twitter:', it_companies)

print()

it_companies.update(['Tesla', 'Sony'])
print('We added Tesla and Sony:', it_companies)

print()

it_companies.remove('Twitter')
print('We removed Twitter:', it_companies)

print()

print('The difference between remove and discard is that the first will throw an error if the item removed does not exist, the second does not.')

print()

print('Join A and B', A.union(B))

print()

print('A intersection B', A.intersection(B))

print()

print('Is A subset of B?', A.issubset(B))

print()

print('Are A and B disjoint:', A.isdisjoint(B))

print()

print('Join A with B and B with A:', A.union(B))

print()

print('Symmetric difference between A and B:', A.symmetric_difference(B))

print()

del A, B

age_set = set(age)
print('Is age list bigger than age_set?', len(age) > len(age_set))

print()

print('Differences between staring, list, tuple, and set:\nstring is text\nlist is a mutable ordered collection\ntuple is a fixed ordered collection\nset is a unique unordered collection')

print()

sentence = 'I am a teacher and I love to inspire and teach people.'
sentence_list = sentence.split()
sentence_set = set(sentence_list)
print(sentence_set)
print('Unique words in sentence:', len(sentence_set))