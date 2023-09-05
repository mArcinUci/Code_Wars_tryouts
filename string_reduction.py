'''In this Kata, we are going to see how a Hash (or Map or dict) can be used to keep track of characters in a string.
Consider two strings "aabcdefg" and "fbd". How many characters do we have to remove from the first string to get the second string?
 Although not the only way to solve this, we could create a Hash of counts for each string and see which character counts are different.
 That should get us close to the answer. I will leave the rest to you.
For this example, solve("aabcdefg","fbd") = 5. Also, solve("xyz","yxxz") = 0, because we cannot get second string from the first
 since the second string is longer.'''

def solve(a,b):
    len_a = len(a)
    len_b = len(b)
    how_many_letters_in_a = {}
    if len_b >= len_a:
        return 0
    else:
        for i in a:
            if i in how_many_letters_in_a:
                how_many_letters_in_a[i] += 1
            else:
                how_many_letters_in_a[i] = 1
        for i in b:
            if i in how_many_letters_in_a.keys():
                how_many_letters_in_a[i] -= 1
    answer = 0
    for i in how_many_letters_in_a.keys():
        if how_many_letters_in_a[i] < 0:
            return 0
        else:
            answer += how_many_letters_in_a[i]      
    return answer   
       
print(solve("abdegfg","ffdb"))  


'''def solve(a,b):
    for x in set(b):
        if a.count(x) >= b.count(x):
            continue
        else:
            return 0
    return len(a)-len(b)'''

'''def solve(a,b):
    a=list(a)
    try:
        for c in b:
            a.pop(a.index(c))
        return len(a)
    except:
        return 0'''