def combine(arr):
    return ' and '.join(', '.join(arr).rsplit(', ', 1))


# def combine(arr):
#     return ' and '.join(', '.join(arr).rsplit(', ', 1))

print(combine(['Python']))
print(combine(['Python', 'Ruby']))
print(combine(['Python', 'Ruby', 'Java']))
print(combine(['Python', 'Ruby', 'Java', 'C#']))
print(combine([]))

# print 'Python, Ruby, Java, C#'.rsplit(', ', 2)

a = ["aaa", "bbb", "ccc", "ddd"]
print(", ".join(a))
print(", ".join(a).rsplit(', ', 1))

s = 'a,b,c,d,e'
print(s.split(',', 2))

