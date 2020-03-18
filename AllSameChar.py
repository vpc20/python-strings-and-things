# def all_same(s):
#     return all([s[0] == s[i] for i in range(1, len(s))])


def all_same(s):
    return len(set(s)) == 1 if s else True


# def all_same(s):
#     for i in range(1, len(s)):
#         if s[i] != s[i - 1]:
#             return False
#     return True


def all_same_recur(s):
    if len(s) < 2:
        return True
    if s[0] != s[1]:
        return False
    return all_same_recur(s[1:])


print(all_same(''))
print(all_same('a'))
print(all_same('aa'))
print(all_same('aaa'))
print('')
print(all_same('ab'))
print(all_same('ba'))
print(all_same('aab'))
print(all_same('aba'))
print(all_same('baa'))
print('')
print(all_same_recur(''))
print(all_same_recur('a'))
print(all_same_recur('aa'))
print(all_same_recur('aaa'))
print('')
print(all_same_recur('ab'))
print(all_same_recur('ba'))
print(all_same_recur('aab'))
print(all_same_recur('aba'))
print(all_same_recur('baa'))

# s = ['a' for i in range(1000000)]
# print(all_same(s))

