def reverse_sentence(s):
    stack = []
    revs = ''
    for i in range(len(s) - 1, -1, -1):
        if s[i].isspace():
            while stack:
                revs += stack.pop()
            revs += s[i]
        else:
            stack.append(s[i])
    while stack:
        revs += stack.pop()
    return revs


# def reverse_sentence(s):
#     return ' '.join(list(reversed(s.split())))

print(reverse_sentence('the quick brown fox'))
