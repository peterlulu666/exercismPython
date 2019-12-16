# def score(word):
#     word = "" + word
#     word = word.upper()
#     one_point_letter = "A, E, I, O, U, L, N, R, S, T"
#     two_point_letter = "D, G"
#     three_point_letter = "B, C, M, P"
#     four_point_letter = "F, H, V, W, Y"
#     five_point_letter = "K"
#     eight_point_letter = "J, X"
#     ten_point_letter = "Q, Z"
#     score_count = 0
#     for letter in word:
#         if letter in one_point_letter:
#             score_count = score_count + 1
#         if letter in two_point_letter:
#             score_count = score_count + 2
#         if letter in three_point_letter:
#             score_count = score_count + 3
#         if letter in four_point_letter:
#             score_count = score_count + 4
#         if letter in five_point_letter:
#             score_count = score_count + 5
#         if letter in eight_point_letter:
#             score_count = score_count + 8
#         if letter in ten_point_letter:
#             score_count = score_count + 10
#     return score_count


# def score(word):
#     word = "" + word
#     word = word.upper()
#     letter_score = dict()
#     letter_score = {"A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
#                     "D": 2, "G": 2,
#                     "B": 3, "C": 3, "M": 3, "P": 3,
#                     "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
#                     "K": 5,
#                     "J": 8, "X": 8,
#                     "Q": 10, "Z": 10}
#     score_count = 0
#     for letter in word:
#         score_count = score_count + letter_score[letter]
#     return score_count


# def score(word):
#     word = "" + word
#     word = word.upper()
#     letter_score = dict()
#     letter_score = {"A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
#                     "D": 2, "G": 2,
#                     "B": 3, "C": 3, "M": 3, "P": 3,
#                     "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
#                     "K": 5,
#                     "J": 8, "X": 8,
#                     "Q": 10, "Z": 10}
#     score_count = []
#     for letter in word:
#         score_count.append(letter_score[letter])
#     return sum(score_count)


# def score(word):
#     word = str(word)
#     word = word.upper()
#     letter_point = {1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
#                     2: ['D', 'G'],
#                     3: ['B', 'C', 'M', 'P'],
#                     4: ['F', 'H', 'V', 'W', 'Y'],
#                     5: ['K'],
#                     8: ['J', 'X'],
#                     10: ['Q', 'Z']}
#     letter_list = []
#     for letter in word:
#         letter_list.append(letter)
#     # letter_list = list(word)
#     score_count = 0
#     for letter in letter_list:
#         for point, character_list in letter_point.items():
#             if letter in character_list:
#                 score_count = score_count + point
#     return score_count


# def score(word):
#     word = str(word)
#     word = word.upper()
#     letter_point = {1: "A, E, I, O, U, L, N, R, S, T",
#                     2: "D, G",
#                     3: "B, C, M, P",
#                     4: "F, H, V, W, Y",
#                     5: "K ",
#                     8: "J, X ",
#                     10: "Q, Z "}
#     letter_list = []
#     for letter in word:
#         letter_list.append(letter)
#     # letter_list = list(word)
#     score_count = 0
#     for letter in letter_list:
#         for point, characters in letter_point.items():
#             if letter in characters:
#                 score_count = score_count + point
#     return score_count


def score(word):
    word = str(word)
    word = word.upper()
    letter_point = {"A, E, I, O, U, L, N, R, S, T": 1,
                    "D, G": 2,
                    "B, C, M, P": 3,
                    "F, H, V, W, Y": 4,
                    "K": 5,
                    "J, X ": 8,
                    "Q, Z ": 10}
    letter_list = []
    for letter in word:
        letter_list.append(letter)
    # letter_list = list(word)
    score_count = 0
    for letter in letter_list:
        for characters, point in letter_point.items():
            if letter in characters:
                score_count = score_count + point
    return score_count
