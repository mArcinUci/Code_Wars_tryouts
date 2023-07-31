def solutions(s):
    ans = []
    alphabet = 'abcdefghijklmnoprstqrstuvwxyz'
    for i in range(len(s)):
        count = len(s)
        slice_s = s[i:count]
        if slice_s in alphabet and count>i:
            ans.append(slice_s)
        else:
            count -= 1

    return ans

print(solutions('xabc'))




'''('xabc',        'xcba'), 
    ('abcxdef',     'cbaxfed'), 
    ('abcxyz',      'cbazyx'), 
    ('zahimzmstaz', 'zaihmzmtsaz'), 
    ('jjjjjjjjklmnopqrstuv', 'jjjjjjjvutsrqponmlkj'), 
    ('zyx',         'zyx'), 
    ('ppqqrr',      'pqprqr'), 
    ('gjaababbboo', 'gjabababboo'),'''