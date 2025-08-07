def text_word_count(text):
    text_list = text.split()
    count = len(text_list)
    print(f"{count} words found in the document")
    return count


def char_nth_times(text):
    char_dict = {}
    for char in text:
        lower_char = char.lower()
        char_dict[lower_char] = char_dict.get(lower_char, 0) + 1 
    
    print(char_dict)
    return char_dict

"""
create a function that will return the number of times a char shown in text including special chars
use .lower()
return a dict with a key:value char: int

"""