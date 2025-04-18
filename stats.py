def get_word_count(text):
    words = text.split()
    return len(words)
        
def get_char_count(text):
    chars={}
    for char in text:
        char = char.lower()
        if char in chars:
            chars[char]+=1
        else:
            chars[char]=1
    return chars
    
def sort_chars(dict):
    char_list=[]
    for i, o in dict.items():
        if i.isalpha():
            char_list.append({"character":i, "count": o})
    def sort_on(dict):
        return dict["count"]
    char_list.sort(reverse=True, key=sort_on)
    return char_list