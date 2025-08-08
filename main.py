from stats import text_word_count, formatted_output, get_book_text
import sys


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)




def main():
    book_text = get_book_text(sys.argv[1])
    formatted_output(book_text)

main()