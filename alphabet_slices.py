def solutions(s):
    ans = []
    alphabet = 'abcdefghijklmnoprstqrstuvwxyz'
    count = 0
    for i in s:
        idx = alphabet.index(i)
        if s[s.index(i) +1]:
            if alphabet[idx+1] == s[s.index(i) +1]:
                ans.append(s[s.index(i) +1])
    print(ans)

solutions('abcxdef')




'''('xabc',        'xcba'), 
    ('abcxdef',     'cbaxfed'), 
    ('abcxyz',      'cbazyx'), 
    ('zahimzmstaz', 'zaihmzmtsaz'), 
    ('jjjjjjjjklmnopqrstuv', 'jjjjjjjvutsrqponmlkj'), 
    ('zyx',         'zyx'), 
    ('ppqqrr',      'pqprqr'), 
    ('gjaababbboo', 'gjabababboo'),'''