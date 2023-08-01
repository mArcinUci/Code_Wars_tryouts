def solutions(s):
    alphabet = 'abcdefghijklmnoprstqrstuvwxyz'
    longest_i_string = []
    slices = []
    string_data = []
    for i in range(len(s)):
        for x in range(i,len(s)+1):   
            slice_s = s[i:x]
            if slice_s in alphabet and x > i and len(slice_s)>1:
                longest_i_string.append([slice_s, x, x-i])
    
    for i in longest_i_string:
        alphabet_string_ending = i[1]
        slice_len = i[2]
        slice_index = [x for x in range(alphabet_string_ending-slice_len, alphabet_string_ending)]       
        string_data.append([i[0],slice_index])    
    

    return string_data

print(solutions('abcxy'))


'''almost_proper_slice_prep = max(map(len,longest_i_string))
    almost_proper_slice = [x for x in longest_i_string if len(x) == almost_proper_slice_prep]'''

'''('xabc',        'xcba'), 
    ('abcxdef',     'cbaxfed'), 
    ('abcxyz',      'cbazyx'), 
    ('zahimzmstaz', 'zaihmzmtsaz'), 
    ('jjjjjjjjklmnopqrstuv', 'jjjjjjjvutsrqponmlkj'), 
    ('zyx',         'zyx'), 
    ('ppqqrr',      'pqprqr'), 
    ('gjaababbboo', 'gjabababboo'),'''


'''for i in range(1,len(longest_i_string)):
        if longest_i_string[i][1] == longest_i_string[i-1][1] and longest_i_string[i][2] > longest_i_string[i-1][2]:
            slices.append(longest_i_string[i][0])'''