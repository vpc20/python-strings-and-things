def mstrip(s, c):
    len1 = len(s) - len(s.lstrip('#'))
    len2 = len(s) - len(s.rstrip('#'))
    return s[:len1] + s.replace(c, '') + s[-len2:]


print(mstrip('###as###df###', '#'))
