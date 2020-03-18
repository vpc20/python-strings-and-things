# def longest_word(s):
#     words = s.split()
#     counts = [len(item) for item in words]
#     idx = counts.index(max(counts))
#     return words[idx]


# def longest_word(s):
#     return s.split()[[len(item) for item in (s.split())].index(max([len(item) for item in (s.split())]))]

def longest_word(s):
    word_len, max_len = 0, 0
    word, max_word = '', ''

    for ch in s:
        if ch.isspace():
            if word_len > max_len:
                max_len = word_len
                max_word = word
            word_len = 0
            word = ''
        else:
            word_len += 1
            word += ch
    return max_word


print(longest_word('The quick brown fox jumps over the lazy dog'))
