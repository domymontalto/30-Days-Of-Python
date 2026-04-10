import json
import re
import csv

with open('Day_19_File_handling/obama_speech.txt', 'r') as f:
    lines = f.readlines()
    words = []
    for sentence in lines:
        words.extend(sentence.split(' '))

    print(f'Number of lines: {len(lines)}')
    print(f'Number of words: {len(words)}')

    print()

with open('Day_19_File_handling/michelle_obama_speech.txt', 'r') as f:
    lines = f.readlines()
    words = []
    for sentence in lines:
        words.extend(sentence.split(' '))

    print(f'Number of lines: {len(lines)}')
    print(f'Number of words: {len(words)}')

print()

with open('Day_19_File_handling/donald_speech.txt', 'r') as f:
    lines = f.readlines()
    words = []
    for sentence in lines:
        words.extend(sentence.split(' '))

    print(f'Number of lines: {len(lines)}')
    print(f'Number of words: {len(words)}')

print()

with open('Day_19_File_handling/melina_trump_speech.txt', 'r') as f:
    lines = f.readlines()
    words = []
    for sentence in lines:
        words.extend(sentence.split(' '))

    print(f'Number of lines: {len(lines)}')
    print(f'Number of words: {len(words)}')

print()

def most_spoken_languages(file_path, n_of_top):

    with open(file_path) as f:
        countries = json.load(f)
        languages_dict = {}
        for country in countries:
            for language in country['languages']:
                if language in languages_dict:
                    languages_dict[language] += 1
                else:
                    languages_dict[language] = 1
    
    sorted_languages = sorted(languages_dict.items(), key= lambda item : item[1], reverse=True)
    return sorted_languages[:n_of_top]       

print(most_spoken_languages('Day_19_File_handling/countries_data.json', 3))

print()

def most_populated_countries(file_path, n_of_top):
    with open(file_path) as f:
        countries = json.load(f)
        countries_list = []
        for country in countries:
            country_info = {'country': country['name'], 'population' : country['population']}
            countries_list.append(country_info)

    countries_list.sort(key= lambda country : country['population'], reverse= True)
    return countries_list[:n_of_top]

print(most_populated_countries('Day_19_File_handling/countries_data.json', 3))

print()

with open('Day_19_File_handling/email_exchanges_big.txt') as f:
    lines = f.readlines()
    email_address = []

    for line in lines:
        text = line.split(' ')
        if text[0] == 'From':
            email_address.append(text[1])

    print(email_address)
    
print()

def find_most_common_words(file_path, n_of_top):

    with open(file_path) as f:
        text = f.read()
        words = re.findall(r'\w+', text)
    
        common_words = {}

        for word in words:
            if word not in common_words:
                common_words[word] = 1
            else:
                common_words[word] += 1
        
        lst_common_words = sorted(common_words.items(), key= lambda item: item[1], reverse=True)
        reversed_lst_common_words = list(map(lambda x: (x[1], x[0]), lst_common_words))
        return reversed_lst_common_words[:n_of_top]

print(find_most_common_words('Day_19_File_handling/obama_speech.txt', 3))
print(find_most_common_words('Day_19_File_handling/michelle_obama_speech.txt', 3))
print(find_most_common_words('Day_19_File_handling/donald_speech.txt', 3))
print(find_most_common_words('Day_19_File_handling/melina_trump_speech.txt', 3))

print()

def top_ten_romeo_words():

    with open('Day_19_File_handling/romeo_and_juliet.txt') as f:

        text = f.read()
        words = re.findall(r'\w+', text)
        dict_words = {}

        for word in words:
            if word in dict_words:
                dict_words[word] +=1
            else:
                dict_words[word] = 1

        lst_words = sorted(dict_words.items(), key= lambda tpl_word : tpl_word[1], reverse= True)
        return lst_words[:10]
    
print(top_ten_romeo_words())

print()

def word_in_file(word):
    with open('Day_19_File_handling/hacker_news.csv') as f:
        csv_reader = csv.reader(f, delimiter= ',')
        tot_word = 0
        word_to_found = word
        
        for row in csv_reader:
            row_text = ' '.join(row)
            if word_to_found in row_text.lower():
                tot_word += 1

        return tot_word
    
print(word_in_file('python'))
print(word_in_file('javascript'))
print(word_in_file('java'))