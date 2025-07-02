def count_words(book):
    book_as_list = book.split()
    book_length = len(book_as_list)
    return book_length

def count_char(book):
    empty_dict = {}
    book_as_list = list(book)
    for string in book_as_list:
        string_in_lowercase = string.lower()
        for string in string_in_lowercase:
            if string in empty_dict:
                empty_dict[string] += 1
            else:
                empty_dict[string] = 1
    return empty_dict

def sort_dict(dict):
    new_list = []
    for key, value in dict.items():
        if key.isalpha():
            small_dict = {"char": key, "num": value}
            new_list.append(small_dict)
    new_list.sort(key=lambda item: item["num"], reverse=True)
    return new_list