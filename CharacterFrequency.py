# Write a function that takes a piece of text in the form of a string and returns the letter
# frequency count for the text. This count excludes numbers, spaces and all punctuation marks.
# Upper and lower case versions of a character are equivalent and the result should all be in
# lowercase.
#
# The function should return a list of tuples (in Python) or arrays (in other languages)
# sorted by the most frequent letters first. Letters with the same frequency are ordered
# alphabetically. For example:
#
#   letter_frequency('aaAabb dddDD hhcc')
# will return
#
#   [('d',5), ('a',4), ('b',2), ('c',2), ('h',2)]

from collections import Counter


def letter_frequency(text):
    counter = Counter(''.join([ch for ch in text.lower() if ch.isalpha()]))
    l = list(tuple(counter.items()))
    l.sort(key=lambda x: (-x[1], x[0]))
    return l


# from collections import Counter
# from operator import itemgetter
#
# def letter_frequency(text):
#     items = Counter(c for c in text.lower() if c.isalpha()).items()
#     return sorted(
#         sorted(items, key=itemgetter(0)),
#         key=itemgetter(1),
#         reverse=True
#     )

# from collections import Counter
# def letter_frequency(text):
#   return sorted(Counter(filter(str.isalpha,
#                         text.lower())
#                         ).most_common(),
#                 key=lambda t:(-t[1],t[0]))

print(letter_frequency('abc b cc dd'))
print(letter_frequency('wklv lv d vhfuhw phvvdjh'))
