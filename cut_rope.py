'''
Here is a rope with a length of x cm. We will cut it in the following way: each m cm to make a mark, and then each n cm to make a mark. 
Finally, We cut the rope from the marked place. Please calculate that we have a total of several kinds of length of the rope, and 
how many of each kind of rope?
'''


def cut_rope(length, m, n):
    indexes = []
    answeres = {}
    score_m = -1
    score_n = -1
    while score_m < length-m:
        score_m = score_m + m
        indexes.append(score_m)
    while score_n < length-n:
        score_n = score_n + n
        indexes.append(score_n)
    indexes.append(length)
    indexes = list(set(indexes))
    indexes.reverse()

    for i in range(len(indexes) -1):
        rope_chunks = indexes[i] - indexes[i+1] 
        if rope_chunks in answeres:
            answeres[rope_chunks] += 1
        else:
            answeres[rope_chunks] = 1
    final_answer = {str(f'{key}cm'): value for key, value in answeres.items()}

    return final_answer

print(cut_rope( 6, 2, 3))
print(cut_rope( 7, 2, 3))