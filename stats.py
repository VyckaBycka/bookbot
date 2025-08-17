def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def character_count(file_path):
    book_text = get_book_text(file_path)

    output_dictionary = {}
    for char in book_text:
        # Converts character to lowercase
        symbol = char.lower()

        if symbol in output_dictionary:
            output_dictionary[symbol] += 1
        else:
            output_dictionary[symbol] = 1

    return output_dictionary

def character_sort(file_path):

    initial_dictionary = character_count(file_path)

    edited_dictionary = {}
    list_of_dictionaries = []

    for k, v in initial_dictionary.items():
        # print(k, v)
        # Skips character if it is not alphabetical
        if not k.isalpha():
            continue

        temporary_dictionary = {}
        temporary_dictionary["char"] = k
        temporary_dictionary["num"] = v

        # print(temporary_dictionary)

        list_of_dictionaries.append(temporary_dictionary)

        # Loop end

    def sort_on(items):
        return items["num"]

    # print(list_of_dictionaries)

    list_of_dictionaries.sort(reverse=True, key=sort_on)

    # print(list_of_dictionaries)

    for stats_dict in list_of_dictionaries:
        # k, v = stats_dict.items()
        print(f"{stats_dict["char"]}: {stats_dict["num"]}")






