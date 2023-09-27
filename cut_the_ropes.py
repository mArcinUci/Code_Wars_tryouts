'''
You are given N ropes, where the length of each rope is a positive integer. At each step, you have to reduce all the ropes by the 
length of the smallest rope.
The step will be repeated until no ropes are left. Given the length of N ropes, print the number of ropes that are left 
before each step.
For a = [3, 3, 2, 9, 7], the result should be [5, 4, 2, 1]
'''


def cut_the_ropes(arr):
    answer = []
    while len(arr)>0:
        answer.append(len(arr))
        arr = [x-min(arr) for x in arr if (x-min(arr)>0)]
    return answer

print(cut_the_ropes([3, 3, 2, 9, 7]))
print(cut_the_ropes(([1, 2, 3, 4, 3, 3, 2, 1])))






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


