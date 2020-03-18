def atoi(s):
    n = 0
    for i in range(len(s)):
        n += (ord(s[i]) - 48) * 10 ** (len(s) - 1 - i)
    return n


print(atoi('123'))

# print(ord('0') - 48)
# print(ord('1') - 48)
