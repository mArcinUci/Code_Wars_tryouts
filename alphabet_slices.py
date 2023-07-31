def solutions(s):
    ans = []
    count = len(s)
    alphabet = 'abcdefghijklmnoprstqrstuvwxyz'
    for i in range(len(s)):
        slice_s = s[i:count]
        if slice_s in alphabet and count<=i:
            ans.append(slice_s)
        else:
            count -= 1

    if 'abc' in alphabet:
        print(1)
    print(ans)

solutions('xabc')




'''('xabc',        'xcba'), 
    ('abcxdef',     'cbaxfed'), 
    ('abcxyz',      'cbazyx'), 
    ('zahimzmstaz', 'zaihmzmtsaz'), 
    ('jjjjjjjjklmnopqrstuv', 'jjjjjjjvutsrqponmlkj'), 
    ('zyx',         'zyx'), 
    ('ppqqrr',      'pqprqr'), 
    ('gjaababbboo', 'gjabababboo'),'''