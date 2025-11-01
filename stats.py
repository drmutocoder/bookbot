# this is likely not proper to have the function to open the book here but in a way I'm glad to understand how to do it in this window.

#learning is learning after all.


def open_book(path):

    with open(path) as f:
        file_contents = f.read()
    
    return file_contents

def count_words(get_book):
    a = get_book.split()
    return len(a)


def count_letters(get_book):
    char = {}
    for i in get_book:
        lowered = i.lower()
        if lowered in char:
            char[lowered] += 1
        else:
            char[lowered] = 1
    print(char)
    return char

def sort_numbers(count_letter):
    return count_letter["num"]


def sorted_count_letters(count_letter):
    l1 = []

    for i in count_letter:
        l1.append(count_letter)

    l1.sort(reverse =True, key=sort_numbers)
    print(l1)

    


