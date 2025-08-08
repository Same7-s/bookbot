from stats import text_word_count, formatted_output


def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
        return file_content

BOOK_PATH = "./books/frankenstein.txt"
frankenstein_book_text = get_book_text(BOOK_PATH)
text_count = text_word_count(frankenstein_book_text)


def main():
    
    formatted_output(frankenstein_book_text)

main()