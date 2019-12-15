def is_isogram(words):
    words = words.replace(" ", "")
    words = words.replace("-", "")
    words = words.lower()
    for letter_index in range(0, len(words)):
        count = 0
        for words_index in range(0, len(words)):
            if words[letter_index] == words[words_index]:
                count = count + 1
        if count > 1:
            return False
    return True


# def is_isogram(words):
#     words = words.lower()
#     for letter_index in range(0, len(words)):
#         count = 0
#         for words_index in range(0, len(words)):
#             if (words[letter_index]).isalpha():
#                 if words[letter_index] == words[words_index]:
#                     count = count + 1
#         if count > 1:
#             return False
#     return True



