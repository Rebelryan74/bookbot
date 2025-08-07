def word_count(book):
    return len(book.split())

def char_count(book):
    character = {}
    new_char = ""
    for char in book:
        new_char = char.lower()
        if new_char in character:
            character[new_char] += 1
        else:
            character[new_char] = 1
    return character

"""def sorted_list(character):
    filtered= []
    for key, value in character.items():
        if key.isalpha():
            filtered.append({"char": key, "num": value})

    sorted_list = sorted(filtered, key=lambda item: item["num"], reverse=True)
    for item in sorted_list:
        (f'{item["char"]}, {item["num"]}')
    return item"""

def sorted_list(character):
    filtered= []
    for key, value in character.items():
        if key.isalpha():
            filtered.append(f'{key}: {value}')
    
    sorted_list = sorted(filtered, key=lambda item: int(item.split(": ")[1]), reverse=True)
    return sorted_list

