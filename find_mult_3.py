'''
Given a certain number, how many multiples of three could you obtain with its digits?
We need a function that can receive a number ann may output in the following order:
-the amount of multiples (that are multiple of three)
-the maximum multiple
'''



from itertools import permutations



def find_mult_3(num):
    all_perm = []
    num = str(num)
    for i in range(1,len(num)+1):
        all_perm += list(permutations(num,i))
    
    all_perms_str = [''.join(str(e) for e in perm) for perm in all_perm]
    all_perms_str = [int(x) for x in all_perms_str]
    all_perms_str = list(set(all_perms_str))
    all_perms_int_div_by_3 = [x for x in all_perms_str if x%3 ==0 and x != 0]
    
    return [len(all_perms_int_div_by_3), max(all_perms_int_div_by_3)]

print(find_mult_3(362))
print(find_mult_3(6063))