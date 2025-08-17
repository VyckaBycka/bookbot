import sys

from stats import get_book_text, character_count, character_sort

def main():

    # print(sys.argv)
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # file_path = "books/frankenstein.txt"
    # Uses second argument from sys.argv as a file path
    file_path = sys.argv[1]

    book_text = get_book_text(file_path=file_path)
    # print(book_text.split())

    word_count = 0
    for word in book_text.split():
        # print(word)
        word_count += 1

    # print(f"{word_count} words found in the document")

    # character_count_dict = character_count(file_path)
    # print(character_count_dict)

    # character_sort

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    character_sort(file_path=file_path)
    print("============= END ===============")

main()
