from stats import get_word_count, get_char_count

def get_book_text(book):
    file_contents=""
    with open(book) as f:
        file_contents = f.read()
    return file_contents
def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    
    word_count = get_word_count(text)
    print(f"{word_count} words found in the document")
    
    char_count = get_char_count(text)
    print(char_count)
    
if __name__ == "__main__":
    main()

