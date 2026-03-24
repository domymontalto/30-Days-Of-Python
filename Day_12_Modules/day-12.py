import random
import string

def random_user_id():
    num_one = random.randint(0, 9)
    letter_one = random.choice(string.ascii_lowercase)
    letter_two = random.choice(string.ascii_lowercase)
    num_two = random.randint(0, 9)
    num_three = random.randint(0, 9)
    letter_three = random.choice(string.ascii_lowercase)

    return str(num_one) + letter_one + letter_two + str(num_two) + str(num_three)  + letter_three

print(random_user_id())

print()

def user_id_gen_by_user():
    letters_and_digits = string.ascii_lowercase + string.digits
    n_char = int(input('How many characters? '))
    n_ids = int(input('How many ids? '))

    for n in range(0, n_ids):
        characters = ''.join(random.choices(letters_and_digits, k = n_char))
        print(characters)

user_id_gen_by_user()

print()

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'rgb({r},{g},{b})'

print(rgb_color_gen())

print()

def list_of_hexa_colors():
    numbers_and_letters = ['a', 'b', 'c', 'd', 'e', 'f'] + list(string.digits)
    rand_numbers_and_letters = ''.join(random.choices(numbers_and_letters, k = 6))
    return ['#' + rand_numbers_and_letters]

print(list_of_hexa_colors())

print()

def generate_colors(type, number):
    lst_colors = []

    if type.lower() == 'rgb':
        for i in range(number):
            lst_colors.append(rgb_color_gen())
    elif type.lower() == 'hexa':
        for i in range(number):
            str_hexa = ''.join(list_of_hexa_colors())
            lst_colors.append(str_hexa)
    return lst_colors

print(generate_colors('hexa', 3))

print()

def shuffle_list(lst):
    random.shuffle(lst)
    return lst

print(shuffle_list([1, 2, 3, 4]))

print()

def random_seven():
    number_set = set()
    while len(number_set) < 7:
        num = random.randint(0,9)
        number_set.add(num)
    num_lst = list(number_set)
    return num_lst

print(random_seven())
