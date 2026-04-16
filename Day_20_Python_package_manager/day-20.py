import requests
import statistics
import re

url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url)
cats = response.json()
cat_weights = []

for cat in cats:
    weight_range = cat['weight']['metric']
    numbers = re.findall(r'\d+', weight_range)
    weight = (int(numbers[0]) + int(numbers[1])) / 2
    cat_weights.append(weight)

print(f'min: {min(cat_weights)}')
print(f'max: {max(cat_weights)}')
print(f'mean: {sum(cat_weights) / len(cat_weights)}')
print(f'median: {statistics.median(cat_weights)}')
print()

cat_lifespan = []

for cat in cats:
    life_span_range = cat['life_span']
    numbers = re.findall(r'\d+', life_span_range)
    lifespan = (int(numbers[0]) + int(numbers[1])) / 2
    cat_lifespan.append(lifespan)

print(f'min: {min(cat_lifespan)}')
print(f'max: {max(cat_lifespan)}')
print(f'mean: {sum(cat_lifespan) / len(cat_lifespan)}')
print(f'median: {statistics.median(cat_lifespan)}')
print()