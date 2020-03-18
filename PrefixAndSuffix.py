def get_all_substring(s):
    return [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]


def get_prefixes(s):
    return [s[:i] for i in range(1, len(s) + 1)]


def get_proper_prefixes(s):
    return [s[:i] for i in range(1, len(s))]


def get_suffixes(s):
    return [s[i:] for i in range(len(s))]


def get_proper_suffixes(s):
    return [s[i:] for i in range(1, len(s))]


def longest_common_prefix(s1, s2):
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            break
    # i = 0
    # while i < len(s1) and s1[i] == s2[i]:
    #     i += 1
    return s1[:i]


# print(get_all_substring('abcde'))

# print(get_prefixes('abcde'))
# print(get_proper_prefixes('abcde'))

# print(get_suffixes('abcde'))
# print(get_proper_suffixes('abcde'))

print(longest_common_prefix('abcdefg', 'abcdxxx'))
