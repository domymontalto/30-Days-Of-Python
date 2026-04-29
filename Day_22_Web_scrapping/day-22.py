import requests
from bs4 import BeautifulSoup
import json
import os

url = 'http://www.bu.edu/president/boston-university-facts-stats/'


response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
os.system('clear')

title = soup.title
title_text = soup.title.get_text()
body = soup.body.get_text()
status = response.status_code

data = {
    'title': title_text,
    'body' : body,
    'status' : status
}

with open('Day_22_Web_scrapping/Boston_university.json', 'w') as f:
    json.dump(data, f, indent= 4)

with open('Day_22_Web_scrapping/Boston_university.json', 'r') as f:
    data = json.load(f)
    print(data)

print()
print()

url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
}

response = requests.get(url, headers=headers)
content = response.text
soup = BeautifulSoup(response.text, 'html.parser')
os.system('clear')
status = response.status_code
title = soup.title
title_text = soup.title.get_text()
body = soup.body.get_text()

tables = soup.find_all('table')
table = tables[0]
rows = table.find_all('tr')[1:]

all_presidents = []

for row in rows:
    president = {}

    cells = row.find_all(['th', 'td'])
    
    if len(cells) < 4:
        continue

    president['name'] = cells[2].get_text(strip=True)
    president['term'] = cells[3].get_text(strip=True)

    all_presidents.append(president)


with open('Day_22_Web_scrapping/President_list.json', 'w') as f:
    json.dump(all_presidents, f, indent= 4)

with open('Day_22_Web_scrapping/Boston_university.json', 'r') as f:
    all_presidents = json.load(f)
    print(all_presidents)

