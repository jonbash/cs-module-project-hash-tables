ignored_chars = [
    '"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}',
    '(', ')', '*', '^', '&'
]


def check_word(word, word_counts):
    word = word.lower()
    for char in word:
        if char in ignored_chars:
            word = word.replace(char, '')
    if word == "":
        return
    elif word_counts.get(word) is None:
        word_counts[word] = 1
    else:
        word_counts[word] += 1


def word_count(s):
    words = s.split()
    word_counts = {}
    for word in words:
        check_word(word, word_counts)
    return word_counts


def sort_word_count_pairs(arr):
    if len(arr) <= 1:  # already sorted
        return arr

    # merge-sort each half
    mid = len(arr) // 2
    arrA = sort_word_count_pairs(arr[:mid])
    arrB = sort_word_count_pairs(arr[mid:])

    # merge
    merged = []
    i = j = 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i][1] > arrB[j][1]:
            merged.append(arrA[i])
            i += 1
        else:
            merged.append(arrB[j])
            j += 1
    # append any leftover elements if necessary
    if i < len(arrA):
        merged.extend(arrA[i:])
    if j < len(arrB):
        merged.extend(arrB[j:])

    return merged


def word_count_histogram(s):
    word_counts = word_count(s)
    longest_word = ""

    for word in word_counts.keys():
        if len(word) > len(longest_word):
            longest_word = word

    word_count_pairs = sort_word_count_pairs(list(word_counts.items()))

    output_string = ""
    for pair in word_count_pairs:
        space_count = len(longest_word) - len(pair[0]) + 2
        output = pair[0] + (" " * space_count) + ("#" * pair[1])
        output_string += output + '\n'
    return output_string


with open("robin.txt") as f:
    s = f.read()
    hist = word_count_histogram(s)
    print(hist)
