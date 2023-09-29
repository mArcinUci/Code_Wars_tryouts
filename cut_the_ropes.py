'''
You are given N ropes, where the length of each rope is a positive integer. At each step, you have to reduce all the ropes by the 
length of the smallest rope.
The step will be repeated until no ropes are left. Given the length of N ropes, print the number of ropes that are left 
before each step.
For a = [3, 3, 2, 9, 7], the result should be [5, 4, 2, 1]
'''

def cut_the_ropes(arr):
    answer = []
    for _ in range(len(arr)):
        if len(arr) > 0:
            answer.append(len(arr))
            min_arr = min(arr)
            arr = [x-min_arr for x in arr if (x-min_arr>0)]
    return answer

print(cut_the_ropes([3, 3, 2, 9, 7]))
print(cut_the_ropes(([1, 2, 3, 4, 3, 3, 2, 1])))





#one of my previous attempts
'''
def cut_the_ropes(arr, ans = None):
    if ans is None:
        ans = []
    if len(arr) > 0:
        ans.append(len(arr))
        min_lenght = min(arr)
        
        for i in arr:
            if i - min_lenght > 0:
                arr[arr.index(i)] = i - min_lenght
            else:
                arr[arr.index(i)] = 0
        arr = [x for x in arr if x != 0]
        return cut_the_ropes(arr,ans)
    else:
        return ans
'''


#somehow this one worked (and my while loop was with -timeout problem-
'''
def cut_the_ropes(a):
    result = []
    while a:
        result.append(len(a))
        m = min(a)
        a = [x-m for x in a if x > m]
    return result'''


'''
def cut_the_ropes(arr):
    qty = len(arr)
    sorted_ropes = sorted(arr)
    return [qty - sorted_ropes.index(n) for n in sorted(set(arr))]
'''

'''
def cut_the_ropes(a):
    if not a:
        return []
    m = min(a)
    return [len(a)] + cut_the_ropes([x-m for x in a if x > m])
'''