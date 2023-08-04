

def accum(s):
    new_s = []
    for x in range(len(s)):
        new_s.append(s[x].upper() + s[x].lower()*(x))
    return '-'.join(new_s)


print(accum("abcd"))