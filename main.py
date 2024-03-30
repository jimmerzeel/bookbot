def main():
    book_path = "books/frankenstein.txt"
    contents = read_books(book_path)
    #print(contents)
    #print(f"{count_words(contents)} words found in the document")
    #print(count_character(contents))
    report(book_path)

def count_words(text):
    words = text.split()
    return len(words)

def count_character(text):
    text = text.lower()
    char_count = {}
    appeared = []
    
    for i in range(0, len(text)):
        if text[i] not in appeared:
            char_count[text[i]] = 1
            appeared.append(text[i])
        elif text[i] in appeared:
            char_count[text[i]] += 1
    return char_count

def report(file_path):
    contents = read_books(file_path)
    char_count_list = list(count_character(contents).items())
    sorted_char_count = sorted(char_count_list, key=lambda x: x[1], reverse=True)

    letters = "abcdefghijklmnopqrstuvwxyz"
    
    print(f"--- Begin report of {file_path} ---")
    print(f"{count_words(contents)} words found in the document\n")

    for character in sorted_char_count:
        if character[0] in letters:
            print(f"The '{character[0]}' character was found {character[1]} times")
    
    print("--- End report ---")

def read_books(path):
    with open(path) as f:
        return f.read()

main()