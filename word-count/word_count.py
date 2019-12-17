def count_words(sentence):
    sentence = "" + sentence
    sentence = sentence.lower()
    letter_list = []
    for letter in sentence:
        # If character is numbers, alphabet letters or a single apostrophe
        # append the character to the list
        if letter.isalnum() or letter == "'":
            letter_list.append(letter)
        # Replace other characters by space and append the space to the list
        else:
            letter_list.append(" ")
    # List of character to string
    # Join character and space
    words_string = ""
    words_string = words_string.join(letter_list)
    # String to list of string
    # Use space as separator to split the words and store the words to the words list
    words_list = []
    words_list = words_string.split()
    # words_list = clean_words(sentence)
    # Count words frequency
    # Create a dictionary and use it as counter
    count = dict()
    for word in words_list:
        word = word.strip("'")
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
        # # We would use get() function to make it more concisely.
        # # The function look up the key and returns the corresponding value.
        # # If the key does not exist in the dictionary it returns default value.
        # count[word] = count.get(word, 0) + 1
    # count = dict()
    # count = words_frequency(words_list)
    return count


def clean_words(sentence):
    sentence = str(sentence)
    letter_list = []
    for letter in sentence:
        # If character is numbers, alphabet letters or a single apostrophe
        # append the character to the list
        if letter.isalnum() or letter == "'":
            letter_list.append(letter)
        # Replace other characters by space and append the space to the list
        else:
            letter_list.append(" ")
    # List of character to string
    # Join character and space
    words_string = ""
    words_string = words_string.join(letter_list)
    # String to list of string
    # Use space as separator to split the words and store the words to the words list
    words_list = []
    words_list = words_string.split()
    return words_list


def words_frequency(words_list):
    count = dict()
    for word in words_list:
        word = word.strip("'")
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
        # # We would use get() function to make it more concisely.
        # # The function look up the key and returns the corresponding value.
        # # If the key does not exist in the dictionary it returns default value.
        # count[word] = count.get(word, 0) + 1
    return count


def letter_frequency(words):
    words = str(words)
    count = dict()
    for letter in words:
        if letter not in count:
            count[letter] = 1
        else:
            count[letter] = count[letter] + 1
        # count[letter] = count.get(letter, 0) + 1
    return count


def invert_letter_frequency(word_dict):
    word_dict = dict(word_dict)
    inverse = dict()
    # We would use the for loop to traverse the dictionary.
    for word_character in word_dict:
        # We would swap the key character with the value number in word dictionary.
        # The word[word_character] is the value in word dictionary.
        # We would create inverse_number variable to store the value.
        inverse_number = word_dict[word_character]
        if inverse_number not in inverse:
            # The inverse_number would be the key in inverse dictionary.
            # The inverse_number did not exist in the inverse dictionary.
            # The inverse[inverse_number] is the value in inverse dictionary.
            # We would store the first character in the value list.
            inverse[inverse_number] = [word_character]
        else:
            # We would append the next character to the value list.
            inverse[inverse_number].append(word_character)
    return inverse
