def solutions(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s = s+'1'
    ans = []
    j =[]
    for i in range(len(s)-1):
        if (ord(s[i])+1 == ord(s[i+1])):
            temporary = ''
            ans.append(i)
            temporary += str(s[i])
            while (ord(s[i])+1 == ord(s[i+1])):
                i+=1
                ans.append(i)
                temporary += str(s[i])
            j.append([temporary])
            
                
            print(temporary) 
    print(j)     
    ans = list(set(ans))


    return ans







print(solutions('abcxdef'))


'''('xabc',        'xcba'), 
    ('abcxdef',     'cbaxfed'), 
    ('abcxyz',      'cbazyx'), 
    ('zahimzmstaz', 'zaihmzmtsaz'), 
    ('jjjjjjjjklmnopqrstuv', 'jjjjjjjvutsrqponmlkj'), 
    ('zyx',         'zyx'), 
    ('ppqqrr',      'pqprqr'), 
    ('gjaababbboo', 'gjabababboo'),'''