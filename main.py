import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]


from stats import count_words
from stats import count_char
from stats import sort_dict

def get_book_text(path):
    file_contents = None
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def main():
    book = get_book_text(book_path)
    book_length = count_words(book)
    book_chars_dict = count_char(book)
    test = sort_dict(book_chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_length} total words")
    print("--------- Character Count -------")
    for value in test:
        print(f"{value["char"]}: {value["num"]}")
    print("============= END ===============")


main()