def get_num_words(book_text):
    word_list = book_text.split()
    num_words = len(word_list)
    return num_words

def count_characters(book_text):
    counts = {}
    lower_case = book_text.lower()
    for char in lower_case:
        if char in counts:
            counts[char] +=1
        else:
            counts[char] = 1
    return counts

def dict_to_list(count_dict: dict):
    list_out = []
    for key, value in count_dict.items():
        if key.isalpha() == True:
            list_out.append({'char': key, 'num': value})
        else:
            pass    
    return list_out
def sort_on(count_dict):
    return count_dict['num']

def print_report(count_dict, file_path, text):
    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at {file_path}...\n")
    print("----------- Word Count ----------\n")
    print(f"Found {get_num_words(text)} total words\n")
    print("--------- Character Count -------\n")
    count_list = dict_to_list(count_dict)
    count_list.sort(reverse = True, key = sort_on)
    for dict in count_list:
        print(f"{dict['char']}: {dict['num']}" )

