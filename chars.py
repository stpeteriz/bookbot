def get_char_count():
    
    def get_book_text(book):
        file_contents=""
        with open(book) as f:
            file_contents = f.read()
        return file_contents
    
    def char_count(book):
        text=get_book_text(book)
        chars={}
        counter=1
        for i in text:
            char=i.lower()
            if char in chars:
                chars[char]+=counter
            else:
                chars[char]=counter
        return chars
    
    def main():
        book="books/frankenstein.txt"
        print(char_count(book))
    
    
    main()