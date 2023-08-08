'''Imagine that you are given two sticks. You want to end up with three sticks of equal length. You are allowed to cut either or both 
of the sticks to accomplish this, and can throw away leftover pieces.'''


def maxlen(L1,L2):
    len_1 = L1
    len_2 = L2
    
    if len_1 > len_2:
        if 2*len_2 <= len_1:
            return len_2
        else:
            for i in range(len_2):
                x = (len_1 / 2) - i
                if x <= len_2:
                    return x
    
    if len_1 < len_2:
        if 2*len_1 <= len_2:
            return len_1
        else:
            for i in range(len_1):
                x = (len_2 / 2) - i
                if x <= len_1:
                    return x
    if len_1 == len_2:
        return len_1 / 2

print(maxlen(8,8))