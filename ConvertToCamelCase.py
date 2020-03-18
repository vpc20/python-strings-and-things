def to_camel_case(s):
    words = s.split('_')
    return words[0].lower() + ''.join([words[i].title() for i in range(1, len(words))])


print(to_camel_case(''))
print(to_camel_case('a'))
print(to_camel_case('A'))
print(to_camel_case('a_b_c'))
print(to_camel_case('camel'))
print(to_camel_case('Camel'))
print(to_camel_case('camel_case'))