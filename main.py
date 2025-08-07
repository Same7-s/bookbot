BOOKS_PATH = "./books/frankenstein.txt"


def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
        print(file_content)
        return file_content




def main():
    get_book_text(BOOKS_PATH)


main()