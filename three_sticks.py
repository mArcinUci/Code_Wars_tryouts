'''Imagine that you are given two sticks. You want to end up with three sticks of equal length. You are allowed to cut either or both 
of the sticks to accomplish this, and can throw away leftover pieces.'''


def maxlen(L1,L2):

    if L1 == L2:
        return L1 / 2

    if L1 > L2 and L1/3 >= L2:
        return L1/3
    if L1 > L2 and L2*2 < L1:
        return L2
    if L1 > L2 and L1/2 < L2:
        return L1/2
    
    if L2 > L1 and L2/3 >= L1:
        return L2/3
    if L2 > L1 and L1*2 < L2:
        return L1
    if L2 > L1 and L2/2 < L1:
        return L1/2
            


print(maxlen(12,5))
