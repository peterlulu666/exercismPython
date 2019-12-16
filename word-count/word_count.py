def count_words(sentence):
    sentence = "" + sentence
    sentence = sentence.lower()
    letter = ""
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
    words = ""
    words = words.join(letter_list)
    # Use space as separator and store the words to the words list
    words_list = []
    words_list = words.split()
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
    return count