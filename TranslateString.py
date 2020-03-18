def translate_(s, old, new):
    d = {}  # translation dictionary
    for i in range(len(old)):
        d[old[i]] = new[i]
    return ''.join([d[ch] if ch in d else ch for ch in s])


print(translate_('abcdef', 'abc', 'xyz'))


table = ''.maketrans('abc', 'xyz')
print('abcdef'.translate(table))
