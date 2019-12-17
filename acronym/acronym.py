# def abbreviate(words):
#     words = str(words)
#     words = words.upper()
#     words = words.replace("'", "")
#     words = words.replace("_", "")
#     words = words.replace(" - ", " ")
#     words = words.replace("-", " ")
#     words_list = words.split(" ")
#     acronym = ""
#     for word in words_list:
#         acronym = acronym + word[0]
#     return acronym


def abbreviate(words):
    words = str(words)
    words = words.upper()
    letter_list = list()
    for letter in words:
        if letter.isalpha() or letter == " ":
            letter_list.append(letter)
        elif letter == "-":
            letter_list.append(" ")
        else:
            letter_list.append("")
    words_string = ""
    words_string = words_string.join(letter_list)
    words_list = []
    words_list = words_string.split()
    # words_list = clean_words(words)
    acronym = ""
    for word in words_list:
        acronym = acronym + word[0]
    return acronym


def clean_words(words):
    words = str(words)
    letter_list = []
    for letter in words:
        if letter.isalpha() or letter == " ":
            letter_list.append(letter)
        elif letter == "-":
            letter_list.append(" ")
        else:
            letter_list.append("")
    words_string = ""
    words_string = words_string.join(letter_list)
    words_list = []
    words_list = words_string.split()
    return words_list
