from stats import get_num_words
from stats import get_book_text
from stats import get_num_letters



l1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

d1 = {}

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters =get_num_letters(text)
    print(f"Found {num_words} total words")
    
    for i in range(len(num_letters)):
        d1 = {l1[i]:num_letters[i]}
        print(d1)





main()
