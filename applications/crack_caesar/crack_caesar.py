# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

letters = [
    'E',
    'T',
    'A',
    'O',
    'H',
    'N',
    'R',
    'I',
    'S',
    'D',
    'L',
    'W',
    'U',
    'G',
    'F',
    'B',
    'M',
    'Y',
    'C',
    'P',
    'K',
    'V',
    'Q',
    'J',
    'X',
    'Z'
]


def translate_text(enc_text, key):
    output = ""
    for char in enc_text:
        new_char = key.get(char)
        output += char if new_char is None else new_char
    return output


def find_cipher_key(enc_text):
    char_freqs = {}

    for char in enc_text:
        char = char.upper()
        if char not in letters:
            continue
        current_freq = char_freqs.get(char)
        if current_freq is None:
            char_freqs[char] = 1
        else:
            char_freqs[char] = current_freq + 1
    char_freq_pairs = [(char, char_freqs[char]) for char in char_freqs.keys()]
    char_freq_pairs = sort_char_freq_pairs(char_freq_pairs)

    return {char: letters[i] for i, (char, _) in enumerate(char_freq_pairs)}


def sort_char_freq_pairs(arr):
    if len(arr) <= 1:  # already sorted
        return arr

    # merge-sort each half
    mid = len(arr) // 2
    arrA = sort_char_freq_pairs(arr[:mid])
    arrB = sort_char_freq_pairs(arr[mid:])

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


with open("ciphertext.txt") as f:
    enc_text = f.read()

key = find_cipher_key(enc_text)
dec_text = translate_text(enc_text, key)
print(dec_text)
