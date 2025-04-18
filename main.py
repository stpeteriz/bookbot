from stats import get_word_count, get_char_count, sort_chars
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(book):
    try:
        file_contents=""
        with open(book) as f:
            file_contents = f.read()
        return file_contents
    except FileNotFoundError:
        print("Error: The file was not found. Please provide a valid relative path.")
    except Exception as e:
        print(f"An error occurred: {e}")


def report_printing(book,word_count,chars_sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in chars_sorted:
        print(f"{i['character']}: {i['count']}")
        

def main():
    book=sys.argv[1]
    
    text = get_book_text(book)
    
    word_count = get_word_count(text)
    
    char_count = get_char_count(text)
    
    chars_sorted = sort_chars(char_count)
    
    report_printing(book,word_count,chars_sorted)
    
if __name__ == "__main__":
    main()

