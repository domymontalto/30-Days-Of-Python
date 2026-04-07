import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

words = re.findall(r"\w+", paragraph)
unique_words = list(set(words))
repeted_words = []

for word in unique_words:
    repeted_words.append((words.count(word), word))

repeted_words.sort(reverse=True)
print(repeted_words)

print()

points = ['-12', '-4', '-3', '-1', '0', '4', '8']

sorted_points = list(map(lambda  x : int(x), points))
distance = max(sorted_points) -(min(sorted_points)) 
print(distance)

print()

def is_valid_variable(variable):

    pattern = r'[^0-9-]+'

    valid_variables = re.findall(pattern, variable)

    is_valid = valid_variables == [variable]

    return is_valid

print(is_valid_variable('first_name'))
print(is_valid_variable('first-name'))
print(is_valid_variable('1first_name'))
print(is_valid_variable('firstname'))

print()

def clean_text(sentence):

    clean_sentence = re.sub(r'[^\w\s]', '', sentence)
    return clean_sentence


sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

cleaned_text = clean_text(sentence)
print(cleaned_text)

print()

def most_frequet_words(sentence):
    lst_sentence = sentence.split(' ')
    unique_sentence = list(set(lst_sentence))
    most_frequent = []
    for word in unique_sentence:
        most_frequent.append((lst_sentence.count(word), word))
    
    most_frequent.sort(reverse=True)
    return most_frequent[0:3]


print(most_frequet_words(cleaned_text))


