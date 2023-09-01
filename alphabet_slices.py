def solution(s):
    dummy = None
    for i in range(len(s)-1):
        if ord(s[i])+1 == ord(s[i+1]):
            if dummy is None:
                dummy = i
        elif dummy is not None:
            slice = s[dummy:i+1]
            reversed_slice = slice[::-1]
            s = s[:dummy] + reversed_slice + s[i+1:]
            dummy = None
    if dummy is not None:
        last_slice = s[dummy:]
        last_reversed_slice = last_slice[::-1]
        s = s[:dummy]+last_reversed_slice     
    return s


print(solution('ggabcggabcffbcdxyz'))



'''def solution(s):
    res, cur = [], [s[0]]
    for x in s[1:]:
        if ord(x) - ord(cur[-1]) == 1:
            cur.append(x)
        else:
            res.extend(cur[::-1])
            cur = [x]
    
    return ''.join(res + cur[::-1])'''

'''
def solution(s):
    out = ""
    i = 0
    while len(out) < len(s):
        rev_word, n = rev_ordered(s[i:])
        out += rev_word
        i += n
    return out'''