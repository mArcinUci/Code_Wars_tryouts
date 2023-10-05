'''
Given a certain number, how many multiples of three could you obtain with its digits?
We need a function that can receive a number and may output in the following order:
-the amount of multiples (that are multiple of three)
-the maximum multiple
'''



from itertools import permutations

def find_mult_3(num):
    num_str = str(num)
    all_perms = []

    for r in range(1, len(num_str) + 1):
        all_perms += list(permutations(num_str, r))

    all_perms_int = [int(''.join(perm)) for perm in all_perms]
    all_perms_int = set(all_perms_int)
    all_perms_int_div_by_3 = [x for x in all_perms_int if x % 3 == 0 and x != 0]

    return [len(all_perms_int_div_by_3), max(all_perms_int_div_by_3)]

print(find_mult_3(362))
print(find_mult_3(6063))