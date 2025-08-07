def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = sys.argv[1]
    book = get_book_text(text)
    word = word_count(book)
    characters = char_count(book)
    sorted = sorted_list(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {text}")
    print("----------- Word Count ----------")
    print(f"Found {word} total words")
    print("--------- Character Count -------")
    for line in sorted:
        print(line)
    print("============= END ===============")

from stats import word_count

from stats import char_count

from stats import sorted_list 


main()