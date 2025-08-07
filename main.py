from stats import text_word_count
from stats import char_nth_times


def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
        return file_content

BOOK_PATH = "./books/frankenstein.txt"
frankenstein_book_text = get_book_text(BOOK_PATH)



def main():
    text_word_count(get_book_text(BOOK_PATH))
    char_nth_times(frankenstein_book_text)


main()