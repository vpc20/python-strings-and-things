# def remove_extra_spaces(s):
#     return ' '.join(s.split())


def remove_extra_spaces(s):
    output = ''
    for c in s:
        if c == ' ':
            if output[-1] != ' ':
                output += ' '
        else:
            output += c
    return output


print(remove_extra_spaces('the quick brown'))
print(remove_extra_spaces('the  quick brown'))
print(remove_extra_spaces('the quick  brown'))
print(remove_extra_spaces('the  quick  brown'))
