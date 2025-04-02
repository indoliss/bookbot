from stats import counting_words,counting_letter,sorted_letters
import sys

def get_boot_text(book_path):
    with open (book_path) as f:
        return f.read()

def main():
    
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    
    book_path=sys.argv[1]
    text=get_boot_text(book_path)
    
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    num_words=counting_words(text)
    print("--------- Character Count -------")
    letter_in_book=counting_letter(text)
    liste=sorted_letters(letter_in_book)
    for i in range (0,len(liste)):
        if liste[i]['char'].isalpha():
            print(f"{liste[i]['char']}: {liste[i]['count']}")
   
   
    
   # print(f"{num_words} words found in the document")
    
main()