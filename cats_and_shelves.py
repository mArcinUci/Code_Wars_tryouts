'''An infinite number of shelves are arranged one above the other in a staggered fashion.
The cat can jump either one or three shelves at a time: from shelf i to shelf i+1 or i+3 (the cat cannot climb on the shelf directly above its head)
Find the minimum number of jumps to go from start to finish'''



def solution(start, finish):
    how_many_shelves = finish - start
    
    if how_many_shelves > 2:
        last_jumps = how_many_shelves % 3
        all_jumps_beefore = how_many_shelves / 3
        answer = all_jumps_beefore + last_jumps
        return int(answer)
    else:
        return how_many_shelves