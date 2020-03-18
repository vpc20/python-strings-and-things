# Description:
#
# Write a reverseWords function that accepts a string a parameter, and reverses each word in the string.
# Every space should stay, so you cannot use words from Prelude.
#
# Example:
#
# reverse_words("This is an example!") # returns  "sihT si na !elpmaxe"


# def reverse_words(str):
#     return ' '.join(s[::-1] for s in str.split(' '))


def reverse_words(s):
    stack = []
    revs = ''
    for i in range(len(s)):
        if s[i].isspace():
            while stack:
                revs += stack.pop()
            revs += s[i]
        else:
            stack.append(s[i])
    while stack:
        revs += stack.pop()
    return revs


print(reverse_words("This is an example!"))
# print(reverse_words("double  spaced  words"))
