from stats import count_characters, print_report
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents



def main(path):
    #file_path = input("Please enter file path to book\n")
    #file_path = "books/frankenstein.txt"
    text = get_book_text(path)
    #print(text)
    #print(f"Found {get_num_words(text)} total words")
    #print(count_characters(text))
    print_report(count_characters(text),path, text)

if len(sys.argv) >= 2:
    main(sys.argv[1])
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)