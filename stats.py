def word_count(document):
    total_words = document.split()
    total_count = len(total_words)
    return total_count

def character_count(document):
    char_report = {}
    total_words = document.split()
    
    for word in total_words:
        for char in word:
            if char.lower() in char_report:
                char_report[char.lower()] +=1
            else:
                char_report[char.lower()] = 1
    return char_report

def sorted_list(char_list):
    return char_list["num"]

def dict_to_string(document):
    updated_string = []
    for letter in document:
        counter = document[letter]
        if letter.isalpha():
            updated_dict = {"char": letter, "num": counter}
            updated_string.append(updated_dict)
    updated_string.sort(reverse=True, key=sorted_list)
    return updated_string