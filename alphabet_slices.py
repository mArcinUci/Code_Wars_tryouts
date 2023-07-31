def solutions(s):
    ans = []
    alphabet = 'abcdefghijklmnoprstqrstuvwxyz'
    for i in range(len(s)):
        for x in range(i,len(s)+1):
            slice_s = s[i:x]
            if slice_s in alphabet and x > i:
                ans.append(slice_s)


    return ans

print(solutions('jjjjjjjjklmnopqrstuv'))




'''('xabc',        'xcba'), 
    ('abcxdef',     'cbaxfed'), 
    ('abcxyz',      'cbazyx'), 
    ('zahimzmstaz', 'zaihmzmtsaz'), 
    ('jjjjjjjjklmnopqrstuv', 'jjjjjjjvutsrqponmlkj'), 
    ('zyx',         'zyx'), 
    ('ppqqrr',      'pqprqr'), 
    ('gjaababbboo', 'gjabababboo'),'''