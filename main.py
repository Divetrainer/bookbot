from stats import word_count, character_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

file_path = "books/frankenstein.txt"
document = get_book_text(file_path)
num_words = word_count(document)
print(f"{num_words} words found in the document")
print(character_count(document))