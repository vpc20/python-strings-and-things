from random import choice
import unittest
from random_data import random_string, random_string_len_n


# recursive
# def is_palindrome(s):
#     if len(s) < 2:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return is_palindrome(s[1:-1])s


# iterative
def is_palindrome(s):
    for i in range(int(len(s) / 2)):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True


# def is_palindrome(string):
#     return str(string) == str(string)[::-1]


def create_palindrome():
    s = random_string(15)
    if choice([True, False]):
        return s + s[::-1]
    else:
        return s + random_string(1) + s[::-1]


def all_same(s):
    # print(str(set(s)).lstrip("{'").rstrip("'}"))
    return str(set(s)).lstrip("{'").rstrip("'}") == s[0]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

        # create palindrome
        for _ in range(10000):
            p = create_palindrome()
            print(p)
            self.assertEqual(is_palindrome(p), True)

        # create non-palindrome
        for _ in range(10000):
            p = create_palindrome() + random_string_len_n(1)
            if all_same(p):
                continue
            print(p)
            self.assertEqual(is_palindrome(p), False)

        # random strings
        for _ in range(10000):
            s = random_string(20)
            print(s)
            self.assertEqual(is_palindrome(s), s == s[::-1])


if __name__ == '__main__':
    unittest.main()

# print(is_palindrome(''))
# print(is_palindrome('1'))
# print(is_palindrome('121'))
# print(is_palindrome('12321'))
# print('')
# print(is_palindrome('12'))
# print(is_palindrome('21'))
# print(is_palindrome('1223'))
# print(is_palindrome('12324'))
# print(is_palindrome(12321))

print(create_palindrome())
