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
    return char

def sorted_list_of_dictionaries(count_letter):
    l1 = []
    for i in count_letter:

        dictionary = {
                "char":i,"num":count_letter[i]
                }
        print(dictionary)
        l1.append(dictionary)
    # here's where it gets hazy
    print("and finally, ", dictionary)
    print(l1)

    
    
