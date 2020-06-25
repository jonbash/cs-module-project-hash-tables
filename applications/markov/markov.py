import random


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


def _create_sentence(starts, analysis):
    done = False
    current = None
    quote_opened = False

    while not done:
        if current is None:
            current = random.choice(starts)
            output = []
            candidate = current
        else:
            possibles = analysis[current]
            candidate = random.choice(possibles)

        open_use = _will_open_quote_can_use(candidate, quote_opened)
        if open_use is None:
            if len(output) == 0:
                current = None
            else:
                current = output.pop()
            continue
        elif open_use:
            quote_opened = True

        close_use = _will_close_quote_can_use(candidate, quote_opened)
        if close_use is None:
            if len(output) == 0:
                current = None
            else:
                current = output.pop()
            continue
        elif close_use:
            quote_opened = False

        is_stop = _is_stop_word(candidate)
        if is_stop and quote_opened:
            if len(output) == 0:
                current = None
            else:
                current = output.pop()
            continue
        done = is_stop
        output.append(candidate)
        current = candidate
    return output


def _is_start_word(word):
    return word[0].isupper() or (word[0] == '"' and word[1].isupper())


def _is_stop_word(word):
    ends = ['.', '?', '!']
    return word[-1] in ends or (word[-1] == '"' and word[-2] in ends)


def _will_open_quote_can_use(word, quote_opened):
    if not quote_opened and word[0] == '"':
        return True
    elif word[0] != '"':
        return False
    else:
        return None


def _will_close_quote_can_use(word, quote_opened):
    if word[-1] != '"':
        return False
    elif quote_opened and word[-1] == '"':
        return True
    else:
        return None


def make_random_sentences(count, training):
    analysis = _analyze(training)
    words_list = list(analysis.keys())
    starts = [word for word in words_list if _is_start_word(word)]

    for _ in range(count):
        sentence = _create_sentence(starts, analysis)
        for word in sentence:
            print(word, end=" ")
        print("")


# ####-------------#### #


with open("input.txt") as f:
    words = f.read()
    make_random_sentences(5, words)
