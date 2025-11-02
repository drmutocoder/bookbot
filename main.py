#this from stats is to take "from the stats folder"
#import means you're taking a specific thing
#import open_book means you're taking this particular function

import sys

from stats import open_book 
from stats import count_words
from stats import count_letters
from stats import sorted_list_of_dictionaries 


def main():

    print("Usage: python3 main.py <path_to_book>")
    
    book_path = sys.argv[1]
    get_book = open_book(book_path)
    count_word = count_words(get_book)
    count_letter = count_letters(get_book)
    sorted_list = sorted_list_of_dictionaries(count_letter)

    print(f"Found {count_word} total words")
   #char num 

    for i in sorted_list:
        print(f"{i["char"]}: {i["num"]}")

main()
