# Description:
#
# A pangram is a sentence that contains every single letter of the alphabet at least once.
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
# because it uses the letters A-Z at least once (case is irrelevant).
#
# Given a string, detect whether or not it is a pangram. Return True if it is, False if not.
# Ignore numbers and punctuation.

from string import ascii_lowercase
import unittest
from random import randrange, choice, shuffle


# from collections import Counter
# import string


# def is_pangram(s):
#     return ''.join([ch for ch in (sorted(set(s.lower()))) if ch in ascii_lowercase]) == ascii_lowercase

# def is_pangram(s):
#     return set(string.lowercase) <= set(s.lower())

def is_pangram2(s):
    return set(ascii_lowercase).issubset(s.lower())


# def is_pangram(s):
#     set_lowercase = set(ascii_lowercase)
#     return set_lowercase.intersection(set(s.lower())) == set_lowercase


def is_pangram(s):
    s1 = set(s.lower())
    if len(s1) < 26:
        return False

    alphabet = set(ascii_lowercase)
    for ch in s1:
        alphabet.discard(ch)
    return not bool(alphabet)


def random_strings(maxlen, maxoccur):
    return ' '.join([random_string(maxlen) for i in range(randrange(1, maxoccur + 1))])


def random_string(maxlen):
    return ''.join([choice(ascii_lowercase) for i in range(randrange(1, maxlen + 1))])


# def random_string_len_n(n):
#     return ''.join([choice(ascii_lowercase) for i in range(n)])


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

        # generate pangrams
        for i in range(10000):
            list1 = list(ascii_lowercase + random_string(20))
            shuffle(list1)
            s1 = ''.join(list1)
            print(s1)
            self.assertEqual(is_pangram(s1), is_pangram2(s1))

            # generate random strings
            # for i in range(1000):
            #     s1 = random_string(100)
            #     print s1
            #     self.assertEqual(is_pangram(s1), is_pangram2(s1))

            # # generate random strings with same length
            # for i in range(1000):
            #     n = randrange(10)
            #     s1 = random_string_len_n(n)
            #     s2 = random_string_len_n(n)
            #     print s1, s2
            #     self.assertEqual(is_anagram(s1, s2), sorted(s1.lower()) == sorted(s2.lower()))


            if __name__ == '__main__':
                unittest.main()

                # print is_pangram("The quick brown fox jumps over the lazy dog")
                # print is_pangram("The quick brown fox jumps over the lay dog")
