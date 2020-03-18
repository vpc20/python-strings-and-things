from collections import Counter


def first_recur_char(s):
    seen = set()
    for c in s:
        if c in seen:
            return c
        seen.add(c)
    return ''


def first_non_recur_char(s):
    counter = Counter(s)
    for c in s:
        if counter[c] == 1:
            return c
    return ''


# print(first_recur_char(''))
# print(first_recur_char('abcd'))
# print(first_recur_char('abcdabcd'))

print(first_non_recur_char(''))
print(first_non_recur_char('a'))
print(first_non_recur_char('abcdabcdeab'))
print(first_non_recur_char('aaabbcddde'))
