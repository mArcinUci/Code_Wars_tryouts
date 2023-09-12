'''Imagine a frog sitting on the top of a staircase which has steps number of steps in it.
A frog can jump down over the staircase and at 1 single jump it can go from 1 to maxJumpLength steps down
Your task is to write a function which will calculate the total amount of all possible ways that the frog can
 go from top to the bottom.
'''

import itertools 
def get_number_of_ways(steps, max_jump_length):
    count = 0
    possible_jumps_length = [x for x in range(1,max_jump_length + 1)]
    for j in range(steps//max_jump_length,steps):
        for i in itertools.product(possible_jumps_length, repeat=j):
            if sum(i) == steps:
                count += 1
    return count

print(get_number_of_ways(10, 4))