import sys
# from collections import Counter


def max_occur_char(s):
    count = {}
    max_count = -sys.maxsize
    max_char = ''
    for c in s:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
        if count[c] > max_count:
            max_count = count[c]
            max_char = c
    return max_char, max_count


# def max_occur_char(s):
#     counter = Counter(s)
#     max_count = -sys.maxsize
#     max_char = ''
#     for ch, count in counter.items():
#         if count > max_count:
#             max_count = count
#             max_char = ch
#     return max_char, max_count


print(max_occur_char('thequickbrownfoxjumpsover'))
