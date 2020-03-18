# An anagram is the result of rearranging the letters of a word to produce a new word.
#
# Note: anagrams are case insensitive
#
# Examples
#
# foefet is an anagram of toffee
# Buckethead is an anagram of DeathCubeK
# The challenge is to write the function isAnagram (or is_anagram in Python) to
# return true if the word test is an anagram of the word original and false otherwise.
# The function prototype is as given below:


# def is_anagram(test, original):
#     return sorted(test.lower()) == sorted(original.lower())

# def is_anagram(test, original):
#     char_count_dict = {}
#     for ch in test.lower():
#         if ch in char_count_dict:
#             char_count_dict[ch] += 1
#         else:
#             char_count_dict[ch] = 1
#     for ch in original.lower():
#         if ch in char_count_dict:
#             char_count_dict[ch] -= 1
#             if char_count_dict[ch] < 0:
#                 return False
#         else:
#             return False
#     return True
from random import randrange, choice, shuffle
from string import ascii_lowercase


# import unittest

from collections import Counter


def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    counter = Counter(s1.lower())
    for ch in s2.lower():
        if ch in counter:
            counter[ch] -= 1
            if counter[ch] < 0:
                return False
        else:
            return False
    return True


# def is_anagram(s1, s2):
#     if len(s1) != len(s2):
#         return False
#
#     s2list = list(s2.lower())
#     for c1 in s1.lower():
#         if c1 in s2list:
#             s2list.remove(c1)
#         else:
#             return False
#     return len(s2list) == 0


def is_anagram_recur(s1, s2):
    def _is_anagram_recur(arr1, arr2):
        if not arr1:
            return True
        if arr1[0] in arr2:
            arr2.remove(arr1[0])
            return _is_anagram_recur(arr1[1:], arr2)
        else:
            return False

    if len(s1) != len(s2):
        return False
    return _is_anagram_recur(list(s1.lower()), list(s2.lower()))


def random_string(maxlen):
    return ''.join([choice(ascii_lowercase) for i in range(randrange(1, maxlen + 1))])


def random_string_len_n(n):
    return ''.join([choice(ascii_lowercase) for i in range(n)])


# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, True)
#
#         # generate anagrams
#         for i in range(1000):
#             s1 = random_string(20)
#             s2 = [ch for ch in s1]
#             shuffle(s2)
#             s3 = ''.join(s2)
#             print(s1, s3)
#             self.assertEqual(is_anagram(s1, s3), True)
#
#         # generate random strings
#         for i in range(1000):
#             s1 = random_string(20)
#             s2 = random_string(20)
#             print(s1, s2)
#             self.assertEqual(is_anagram(s1, s2), sorted(s1.lower()) == sorted(s2.lower()))
#
#         # generate random strings with same length
#         for i in range(1000):
#             n = randrange(10)
#             s1 = random_string_len_n(n)
#             s2 = random_string_len_n(n)
#             print(s1, s2)
#             self.assertEqual(is_anagram(s1, s2), sorted(s1.lower()) == sorted(s2.lower()))
#
#
# if __name__ == '__main__':
#     unittest.main()

print(is_anagram('', ''))
print(is_anagram('a', 'a'))
print(is_anagram('ab', 'ab'))
print(is_anagram('ab', 'ba'))
print(is_anagram('abc', 'abc'))
print(is_anagram('abc', 'acb'))
print(is_anagram('abc', 'bca'))
print(is_anagram('abc', 'bac'))
print(is_anagram('abc', 'cab'))
print(is_anagram('abc', 'cba'))
print(is_anagram('Creative', 'Reactive'))
print('')
print(is_anagram('', 'a'))
print(is_anagram('a', ''))
print(is_anagram('a', 'b'))
print(is_anagram('b', 'a'))
print(is_anagram('ab', 'ac'))
print(is_anagram('ab', 'ca'))
print(is_anagram('ab', 'cc'))
print(is_anagram('Creativex', 'Reactive'))
print(is_anagram('Creative', 'xReactive'))
print('')
print(is_anagram_recur('', ''))
print(is_anagram_recur('a', 'a'))
print(is_anagram_recur('ab', 'ab'))
print(is_anagram_recur('ab', 'ba'))
print(is_anagram_recur('abc', 'abc'))
print(is_anagram_recur('abc', 'acb'))
print(is_anagram_recur('abc', 'bca'))
print(is_anagram_recur('abc', 'bac'))
print(is_anagram_recur('abc', 'cab'))
print(is_anagram_recur('abc', 'cba'))
print(is_anagram_recur('Creative', 'Reactive'))
print('')
print(is_anagram_recur('', 'a'))
print(is_anagram_recur('a', ''))
print(is_anagram_recur('a', 'b'))
print(is_anagram_recur('b', 'a'))
print(is_anagram_recur('ab', 'ac'))
print(is_anagram_recur('ab', 'ca'))
print(is_anagram_recur('ab', 'cc'))
print(is_anagram_recur('Creativex', 'Reactive'))
print(is_anagram_recur('Creative', 'xReactive'))
