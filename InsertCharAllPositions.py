# def ins_char(s, c):
#     result = []
#     for i in range(len(s) + 1):
#         result.append(s[:i] + c + s[i:])
#     return result


def ins_char(s, c):
    return [s[:i] + c + s[i:] for i in range(len(s) + 1)]


print(ins_char('', ''))
print(ins_char('', 'x'))
print(ins_char('a', 'x'))
print(ins_char('ab', 'x'))
print(ins_char('abc', 'x'))

print(ins_char('a', ''))
