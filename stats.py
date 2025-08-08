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
    
    # print(char_dict)
    return char_dict

def sort_on(item):
    return item["num"]



def sorted_chars(chars_dict):
    chars_list = []

    for char in chars_dict:
        if char.isalpha():
            char_count = chars_dict[char]
            chars_list.append({
                "char": char,
                "num": char_count
            })
    
    chars_list.sort(reverse=True, key=sort_on)
    print(chars_list)
    return chars_list
    
"""
create a function that will return the number of times a char shown in text including special chars
use .lower()
return a dict with a key:value char: int

"""