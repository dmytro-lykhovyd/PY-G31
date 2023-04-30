import math


# 1
def clock():
    min = int(input('how much minutes have passed?: '))  # assume input is always int digit
    hours = min // 60
    days = hours // 24
    min_left = min - (hours * 60)  # minutes left before next hour
    hours_left = hours - (days * 24)  # hours left before next day
    if 60 <= min <= 1440:
        hours = min // 60
        days = 0
    elif min >= 1440:
        hours = hours_left
        days = min // 1440
    else:
        hours = 0
        days = 0

    print(f'Today has passed {days} days, {hours} hours, {min_left} minutes from zero hour')


clock()


# 2
def what_number_is():
    digit = input('Enter number:  ')
    if not int(digit.isdigit()):
        print('Integer required')
    else:
        digit = int(digit)
        digit_next = digit + 1
        digit_prev = digit - 1
        print(f"The next number for {digit} is {digit_next}. The previous number for {digit} is {digit_prev}")


what_number_is()


# 3
def calculator():
    a = int(input('Enter a: '))
    print('a: ', a)
    b = int(input('Enter b: '))
    print('b: ', b)
    o = input('Enter o: ')
    if o == '+':
        print('a + b = ', a + b)
    elif o == '-':
        print('a - b = ', a - b)
    elif o == '*':
        print('a * b = ', a * b)
    elif o == '/':
        if b != 0:
            print('a / b = ', a / b)
        else:
            print('Division by zero error')
    elif o == 'div':
        if b != 0:
            print('a div b = ', a // b)
        else:
            print('Division by zero error')
    elif o == 'mod':
        if b != 0:
            print('a mod b = ', a % b)
        else:
            print('Division by zero error')
    elif o == 'exp':
        print('a exp b = ', a ** b)


calculator()


# 4
def km_to_miles():
    km = float(input('How much kilometers?:  '))  # how to handle type error?
    print(km * 0.621371)


km_to_miles()


# 5
def cel_to_fahr():
    cel = float(input('How much celsius degree?:  '))
    fahr = cel * 9/5 + 32
    print(f'{cel} C degrees is {fahr} F degrees')


cel_to_fahr()


def triangle_sqr():
    a = float(input('Input first cathetus lenght:  '))
    b = float(input('Input second cathetus lenght:  '))
    sqr = (a * b)/2
    print(f'Square of the right-angled triangle is equal to {sqr}')


triangle_sqr()


#6
def triangle_sqr_by_heron():
    a = 6
    b = 4
    c = 5
    s = (a+b+c)/2  # half-perimeter
    sqr = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f'Triangle square by Heron formula is equal to {sqr}')


triangle_sqr_by_heron()





