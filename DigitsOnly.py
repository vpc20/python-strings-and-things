from string import digits


def is_digits_only(s):
    for c in s:
        if c not in digits:
            return False
    return True


# def is_digits_only(s):
#     return all([c in digits for c in s])


print(is_digits_only('asdf'))
print(is_digits_only('123'))
print(is_digits_only('1a3'))

print('asdf'.isdigit())
print('123'.isdigit())
print('1a3'.isdigit())

