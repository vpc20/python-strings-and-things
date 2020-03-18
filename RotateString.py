# Write a function to rotate the characters in a string n times
# A positive value of n rotates the characters to the right
# A negative value of n rotates the characters to the left
# A zero value of n does not change the value of the string
#
# rotate_string("abcde", 1) ==> "eabcd"
# rotate_string("abcde", 2) ==> "deabc"
# rotate_string("abcde", 3) ==> "cdeab"
# rotate_string("abcde", 4) ==> "bcdea"
# rotate_string("abcde", 5) ==> "abcde"
#
# Assumption : String will not be empty

import unittest


# from collections import deque
# def rotate_string(s, n):
#     dq = deque(s)
#     dq.rotate(n)
#     return ''.join(dq)

def rotate_string(s, n):
    if not s:
        return s
    n %= len(s)
    # return s[len(s) - n:] + s[:len(s) - n]
    return s[-n:] + s[:-n]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual("", rotate_string("", 0))
        self.assertEqual("", rotate_string("", 1))
        self.assertEqual("abcde", rotate_string("abcde", 0))

        self.assertEqual("eabcd", rotate_string("abcde", 1))
        self.assertEqual("deabc", rotate_string("abcde", 2))
        self.assertEqual("cdeab", rotate_string("abcde", 3))
        self.assertEqual("bcdea", rotate_string("abcde", 4))
        self.assertEqual("abcde", rotate_string("abcde", 5))
        self.assertEqual("eabcd", rotate_string("abcde", 6))
        self.assertEqual("deabc", rotate_string("abcde", 7))
        self.assertEqual("cdeab", rotate_string("abcde", 8))
        self.assertEqual("bcdea", rotate_string("abcde", 9))

        self.assertEqual(rotate_string("abcde", -1), "bcdea")
        self.assertEqual(rotate_string("abcde", -2), "cdeab")
        self.assertEqual(rotate_string("abcde", -3), "deabc")
        self.assertEqual(rotate_string("abcde", -4), "eabcd")
        self.assertEqual(rotate_string("abcde", -5), "abcde")
        self.assertEqual(rotate_string("abcde", -6), "bcdea")
        self.assertEqual(rotate_string("abcde", -7), "cdeab")
        self.assertEqual(rotate_string("abcde", -8), "deabc")
        self.assertEqual(rotate_string("abcde", -9), "eabcd")

        self.assertEqual(rotate_string("a", 0), "a")
        self.assertEqual(rotate_string("a", 1), "a")
        self.assertEqual(rotate_string("a", 2), "a")
        self.assertEqual(rotate_string("a", 3), "a")
        self.assertEqual(rotate_string("a", -1), "a")
        self.assertEqual(rotate_string("a", -2), "a")
        self.assertEqual(rotate_string("a", -3), "a")

        self.assertEqual(rotate_string("ab", 0), "ab")
        self.assertEqual(rotate_string("ab", 1), "ba")
        self.assertEqual(rotate_string("ab", 2), "ab")
        self.assertEqual(rotate_string("ab", 3), "ba")
        self.assertEqual(rotate_string("ab", -1), "ba")
        self.assertEqual(rotate_string("ab", -2), "ab")
        self.assertEqual(rotate_string("ab", -3), "ba")


if __name__ == '__main__':
    unittest.main()

# print rotate_string("abcde", 0)
# print rotate_string("abcde", 1)
# print rotate_string("abcde", 2)
# print rotate_string("abcde", 3)
# print rotate_string("abcde", 5)
# print rotate_string("abcde", 6)
# print rotate_string("a", 0)
# print rotate_string("a", 1)
# print rotate_string("a", 2)
# print rotate_string("ab", 0)
# print rotate_string("ab", 1)
# print rotate_string("ab", 2)
# print rotate_string("ab", 3)
# print rotate_string("abc", -1)
# print rotate_string("abc", -2)
# print rotate_string("abc", -3)
