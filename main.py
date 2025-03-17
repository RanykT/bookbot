import sys

if (len(sys.argv) == 2):
    first_arg = sys.argv[1]
    print(f"First argument: {first_arg}")
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import get_num_words
from stats import count_chars

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = count_chars(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in num_chars.items():
        print(f"{char}: {count}")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()
