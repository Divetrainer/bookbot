from stats import word_count, character_count, dict_to_string
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


if len(sys.argv) > 1:
    file_path = sys.argv[1]
    document = get_book_text(file_path)
    num_words = word_count(document)
    characters = character_count(document)
    sorted_chars = dict_to_string(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        print(f"{char["char"]}: {char["num"]}")
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)