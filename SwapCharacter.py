# def swap_char(s, i, j):
#     lst = list(s)
#     lst[i], lst[j] = lst[j], lst[i]
#     return ''.join(lst)


def swap_char(s, i, j):
    if i > j:
        i, j = j, i
    return s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:] if i != j else s


print(swap_char('abcd', 0, 1))
print(swap_char('abcd', 1, 2))
print(swap_char('abcd', 2, 3))

print(swap_char('abcd', 0, 2))
print(swap_char('abcd', 1, 3))

print(swap_char('abcd', 0, 3))
print(swap_char('abcd', 3, 0))
print(swap_char('abcd', 3, 3))
