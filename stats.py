def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
        return file_content


# Counting words in book text
def text_word_count(text):
    text_list = text.split()
    count = len(text_list)
    return count

# Checking how many times each char appears in the text
def char_nth_times(text):
    char_dict = {}
    for char in text:
        lower_char = char.lower()
        char_dict[lower_char] = char_dict.get(lower_char, 0) + 1 
    
    return char_dict

# Sorting dictionary outpu
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
    return chars_list
    
# Formatting the final output

def formatted_output(book):
    
    report_header = "============ BOOKBOT ============\n"\
    f"Analyzing book found at books/frankenstein.txt...\n"\
    "----------- Word Count ----------\n"\
    f"Found {text_word_count(book)} total words\n"\
    "--------- Character Count -------"
    print(report_header)
    
    chars_list = sorted_chars(char_nth_times(book))
    for char in chars_list:
        print(f"{char["char"]}: {char["num"]}")

    print("============= END ===============")



