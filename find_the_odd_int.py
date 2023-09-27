'''
Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.
'''


def find_it(seq):
    max_val = 0
    letters_count = {}
    answer_count = 0

    for i in seq:
        if i in letters_count:
            letters_count[i] += 1
        else:
            letters_count[i] = 1
    for x in letters_count.values():
        if x > max_val and x%2 == 1:
            answer_count = x
    for k,v in letters_count.items():
        if v == answer_count:
            return k

print(find_it(([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])))
print(find_it([5,4,3,2,1,5,4,3,2,10,10]))
print(find_it([10,10,10]))


'''
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
'''

'''
def find_it(seq):
    return [x for x in seq if seq.count(x) % 2][0]
'''