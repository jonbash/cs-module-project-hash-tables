ignored_chars = [
    '"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}',
    '(', ')', '*', '^', '&'
]


def __check_word(word, word_counts):
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
        __check_word(word, word_counts)
    return word_counts


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
