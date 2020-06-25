import random


# TODO: Make sure quotation marks are opened and closed


def _analyze(words):
    word_list = words.split()
    next_words = {}
    for i in range(len(word_list) - 1):
        word = word_list[i]
        next_word = word_list[i + 1]
        if next_words.get(word) is None:
            next_words[word] = [next_word]
        else:
            next_words[word].append(next_word)
    return next_words


def _construct_sentence(analysis):
    words_list = list(analysis.keys())
    starts = [word for word in words_list if _is_start_word(word)]

    current = random.choice(starts)
    done = False
    print(current, end=" ")

    while not done:
        possibles = analysis[current]
        current = random.choice(possibles)
        if _is_stop_word(current):
            done = True
            print(current)
        else:
            print(current, end=" ")


def _is_start_word(word):
    return word[0].isupper() or (word[0] == '"' and word[1].isupper())


def _is_stop_word(word):
    ends = ['.', '?', '!']
    return word[-1] in ends or (word[-1] == '"' and word[-2] in ends)


def make_random_sentences(count, training):
    analysis = _analyze(training)
    for _ in range(count):
        _construct_sentence(analysis)


# ####-------------#### #


# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    make_random_sentences(5, words)
