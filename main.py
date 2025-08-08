from stats import text_word_count
from stats import char_nth_times
from stats import sorted_chars


def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
        return file_content

BOOK_PATH = "./books/frankenstein.txt"



def main():
    frankenstein_book_text = get_book_text(BOOK_PATH)
    text_word_count(frankenstein_book_text)
    char_nth_times(frankenstein_book_text)
    sorted_chars(char_nth_times(frankenstein_book_text))

main()