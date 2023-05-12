
# 1

def is_prime_number(user_digit):
    if user_digit <= 1:
        return False
    for i in range(2, user_digit-1):
        if user_digit % i == 0:
            return False
    return True


user_digit = int(input('Enter number: '.strip()))
if is_prime_number(user_digit):
    print(f'{user_digit} is A prime')
else:
    print(f'{user_digit} is NOT a prime')


print('*' * 40)
# 2


def unpack_tuple_to_vars(raw_tuple):
    (v1, *v3, v4) = raw_tuple
    print(v3)
    print(v4)
    print(type(v4))


raw_tuple = ('one', 'two', 'three', 'five', 'seven', 'eleven')
unpack_tuple_to_vars(raw_tuple)


print('*' * 40)
# 3

def tuple_to_str(raw_tuple):
    [*new_str] = raw_tuple
    new_str = ' '.join(new_str)
    print(new_str)


raw_tuple = ('one', 'two', 'three', 'five', 'seven', 'eleven')
tuple_to_str(raw_tuple)


print('*' * 40)
# 4

def is_element_in_tuple(char, raw_tuple):
    if char in raw_tuple:
        print(True)
    else:
        print(False)


raw_tuple = ('one', 'two', 'three', 'five', 'seven', 'eleven')
char = input('Is element in tuple?: '.strip())
is_element_in_tuple(char, raw_tuple)


print('*' * 40)
# 5

def reverse_tuple(raw_tuple):
    reversed_tuple = raw_tuple[::-1]
    print(reversed_tuple)


raw_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
reverse_tuple(raw_tuple)


print('*' * 40)
# 6

"""returns sorted by ascending list of last elements in list of tuples"""
def sorted_list(first_tuple, second_tuple, third_tuple):
    v_1 = first_tuple[-1]
    v_2 = second_tuple[-1]
    v_3 = third_tuple[-1]

    new_list = [v_1, v_2, v_3]
    new_list.sort()
    print(new_list)


first_tuple = ('one', 'two', 'five')
second_tuple = ('123', 'qwerty')
third_tuple = ('foo', 'baz', 'bar')
sorted_list(first_tuple, second_tuple, third_tuple)


print('*' * 40)
# 7

def is_empty_list(raw_list):
    try:
        raw_list[0]
        print('Not empty')
    except IndexError:
        print('Empty')


raw_list = list()
is_empty_list(raw_list)


print('*' * 40)

# 8

from random import randint


def remove_evens_from_list(raw_list):
    odds_list = [x for x in raw_list if x % 2 != 0]
    return odds_list


"""Let's use generator also for creating list of random integers"""
raw_list = [randint(10, 99) for i in range(20)]
odds_list = remove_evens_from_list(raw_list)
print(raw_list)
print(odds_list)


print('*' * 40)


"""Randomizer Game"""


def randomizer_game(random_num):
    while True:
        user_guess = int(input('For guessing, input your number from 0 to 100: '.strip()))
        if user_guess > random_num:
            print('High')
        elif user_guess < random_num:
            print('Low')
        else:
            print('Exactly')
            break


random_num = randint(1, 100)
randomizer_game(random_num)




