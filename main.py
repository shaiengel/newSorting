import language_dictionary


def language_comparator(s):
    # switch letters of word to the new dictionary
    switched_string = ''.join(language_dictionary.dictionary.get(letter, letter) for letter in s)
    return switched_string.lower()


def sort_by_new_language(str_input):
    # remove all symbols which are not [^a-zA-Z]
    new_str = ''.join(char for char in str_input if char.isalpha() or char == ' ')

    # sort by custom comparator
    input_sorted_str = sorted(new_str.split(), key=language_comparator)

    # return new string
    output_str = ' '.join(input_sorted_str)
    return output_str


if __name__ == '__main__':
    str_input = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
    str_output = sort_by_new_language(str_input)
    print(str_output)
