def count_words(sentence):
    sentence = "" + sentence
    sentence = sentence.lower()
    letter = ""
    letters = []
    for letter in sentence:
        # If character is numbers, alphabet letters or a single apostrophe
        # append the character to the list
        if letter.isalnum() or letter == "'":
            letters.append(letter)
        # Replace other characters by space and append the space to the list
        else:
            letters.append(" ")
    # List of character to string
    # Join character and space
    words = ""
    words = words.join(letters)
    # Use space as separator and store the words to the words list
    words_list = words.split()
    # Create a dictionary and use it as counter
    count = dict()
    for word in words_list:
        # if word not in count:
        #     count[word.strip("'")] = 1
        # else:
        #     count[word.strip("'")] += 1
        count[word.strip("'")] = count.get(word.strip("'"), 0) + 1
    return count
