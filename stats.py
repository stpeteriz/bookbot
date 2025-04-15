def get_num_words():
    
    def get_book_text(book):
        file_contents=""
        with open(book) as f:
            file_contents = f.read()
        return file_contents

    def word_count(book):
        whole=get_book_text(book)
        word_list=whole.split()
        words=len(word_list)
        return words
        


    def main():
        book="books/frankenstein.txt"
        print(f"{word_count(book)} words found in the document")
        
        
    main()