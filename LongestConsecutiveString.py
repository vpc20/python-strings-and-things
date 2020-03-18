# def longest_constr(s):
#     prev_ch = ''
#     str_len = 0
#     max_len = 0
#     max_ch = ''
#
#     for ch in s:
#         if ch != prev_ch:
#             if prev_ch == '':
#                 str_len = 1
#                 prev_ch = ch
#             else:
#                 if str_len > max_len:
#                     max_len = str_len
#                     max_ch = prev_ch
#                 str_len = 1
#                 prev_ch = ch
#         else:
#             str_len += 1
#
#     if str_len > max_len:
#         max_len = str_len
#         max_ch = prev_ch
#
#     return max_ch, max_len


def longest_constr(s):
    if not s:
        return '', 0

    str_len, max_len = 1, 1
    prev_ch, max_ch = s[0], s[0]

    for i in range(1, len(s)):
        if s[i] != prev_ch:
            if str_len > max_len:
                max_len = str_len
                max_ch = prev_ch
            str_len = 1
            prev_ch = s[i]
        else:
            str_len += 1

    if str_len > max_len:
        max_len = str_len
        max_ch = prev_ch

    return max_ch, max_len


# def longest_constr(s):
#     counter = Counter(s)
#     list1 = [(k, v) for k, v in counter.items()]
#     slist1 = sorted(list1, key=lambda e: e[1])
#     return slist1[-1]


# def longest_constr(s):
#     return sorted([(k, v) for k, v in Counter(s).items()], key=lambda e: e[1])[-1]

print(longest_constr('a'))
print(longest_constr('aa'))
print(longest_constr('aaabbcddxxxxz'))
print(longest_constr('aaabbcddxxxxzzzzzz'))
