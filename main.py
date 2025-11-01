#this from stats is to take "from the stats folder"
#import means you're taking a specific thing
#import open_book means you're taking this particular function

from stats import open_book 
from stats import count_words
from stats import count_letters
from stats import sorted_count_letters

def main():
    
    book_path = "books/frankenstein.txt"
    get_book = open_book(book_path)
    count_word = count_words(get_book)
    count_letter = count_letters(get_book)
    sorted_letters = sorted_count_letters(count_letter)

    sort_number = sort_numbers(count_letter)

    print(sort_number)

    
main()
