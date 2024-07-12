import string


def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    word_count = get_word_count(text)
    chars_dict = get_characters_num(text.lower())
    chars_list = sort_characters(chars_dict)
    message(word_count, chars_list)


def message(word_count, chars_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for item in chars_list:
        if item["char"].isalpha():
            print(f"The {item['char']} character was found {item['num']} times")

def sort_characters(chars_dict):
    list = []
    for char in chars_dict:
        list.append({"char": char, "num": chars_dict[char]})
    list.sort(reverse=True, key=lambda x: x["num"]) 
    return list


def get_characters_num(text):
    chars = {}
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def get_word_count(text):
    words = text.split(" ")
    return len(words)

def get_book_text(path):
    with open(path) as f:
        try:
            file_content = f.read()
            return file_content
        except Exception as e:
            print(f"Exception: {e}")

if __name__ == '__main__':
    main()