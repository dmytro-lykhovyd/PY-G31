# 1

def extract_from_string():
    raw_str = 'loremipsum'.strip()
    first = raw_str[0]
    last = raw_str[-1]
    mid_index = len(raw_str) // 2
    mid = raw_str[mid_index]
    extracted_list = [first, mid, last]
    extracted_str = ''.join(extracted_list)
    print(extracted_str)


extract_from_string()


# 2

def is_symmetry():
    raw_str = input('Enter text with even number of symbols: '.strip())
    if len(raw_str) % 2 == 0:
        half_char = len(raw_str) // 2
        first_slice = raw_str[0:half_char]
        second_slice = raw_str[half_char:]
        index = -1

        while index <= half_char:
            index += 1
            if first_slice == second_slice:
                print('The string IS symmetrical')
                break
            else:
                print('The string is NOT symmetrical')
                break
    else:
        print('Error: your input must contain only even number of symbols')


is_symmetry()


# 3

def is_palindrome():
    raw_str = input('Enter text: '.strip())
    half_char = len(raw_str) // 2
    first_slice = raw_str[0:half_char]
    second_slice = raw_str[half_char:]
    reverse_slice = second_slice[::-1]
    index = -1

    while index <= half_char:
        if first_slice == reverse_slice:
            print('The string IS palindrome')
            break
        else:
            print('The string is NOT palindrome')
            break


is_palindrome()
