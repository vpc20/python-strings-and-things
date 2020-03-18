# Remove duplicate characters in a given string keeping only the first occurrences.
# For example, if the input is 'tree traversal' the output will be 'tre avsl'.


def remove_dup(s):
    output = ''
    for ch in s:
        if ch not in output:
            output += ch
    return output


# def remove_dup(s):
#     clist = [c for c in s]
#     return ''.join([clist[i] for i in range(len(clist)) if clist[i] not in clist[:i]])


print(remove_dup('tree traversal'))
