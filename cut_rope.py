'''
Here is a rope with a length of x cm. We will cut it in the following way: each m cm to make a mark, and then each n cm to make a mark. 
Finally, We cut the rope from the marked place. Please calculate that we have a total of several kinds of length of the rope, and 
how many of each kind of rope?
'''


def cut_rope(length, m, n):
    answeres = {}
    indexes = [x for x in range(1,length+1) if x % m == 0 or x % n == 0]
    if length not in indexes:
        indexes.append(length)
    indexes.append(0)
    indexes.sort()

    for i in range(len(indexes)-1):
        rope_chunks = indexes[i+1] - indexes[i]
        if rope_chunks in answeres:
            answeres[rope_chunks] += 1
        else:
            answeres[rope_chunks] = 1
    answeres = dict(sorted(answeres.items()))
    final_answer = {str(f'{key}cm'): value for key, value in answeres.items()}

    return final_answer

print(cut_rope( 1, 7, 19))
print(cut_rope( 7, 2, 3))


'''
def cut_rope(length, m, n):
    from collections import defaultdict
    p, h = 0, defaultdict(int)
    for i in range(1, length + 1):
        if i == length or i % m == 0 or i % n == 0:
            h[f"{i - p}cm"] += 1
            p = i
    return h
'''


'''
from collections import Counter
def cut_rope(l, m, n):
    a = sorted(set(range(0, l, m)) | set(range(0, l, n)) | {l})
    c = Counter([y - x for x, y in zip(a, a[1:])])
    return {f'{k}cm': v for k, v in c.items()}
'''