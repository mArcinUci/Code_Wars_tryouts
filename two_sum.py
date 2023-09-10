'''Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items
 in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple / list
   (depending on your language) like so: (index1, index2).
For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.
The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; 
target will always be the sum of two different items from that array).'''


def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (i,j)
           
print(two_sum([2,2,3],4))


'''def two_sum(nums, t):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == t:
                return [i, j]'''

'''def two_sum(n, target):
    for i in range(len(n)-1):
        if (target-n[i]) in n[i+1:]:
            return [i, n[i+1:].index(target-n[i])+(i+1)]
    return None'''