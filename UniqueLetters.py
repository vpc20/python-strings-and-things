
def unique_letter(s):
    return len(set(s)) == len(s)


print(unique_letter('abcde'))
print(unique_letter('abcbe'))

