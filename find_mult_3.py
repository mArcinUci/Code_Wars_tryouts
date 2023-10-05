'''
Given a certain number, how many multiples of three could you obtain with its digits?
We need a function that can receive a number and may output in the following order:
-the amount of multiples (that are multiple of three)
-the maximum multiple
'''

from itertools import permutations

def find_mult_3(num):
    num_str = str(num)
    all_perms_int_div_by_3 = set()

    for r in range(1, len(num_str) + 1):
        perms = permutations(num_str, r)
        for perm in perms:
            current_num = int(''.join(perm))
            if current_num % 3 == 0 and current_num != 0:
                all_perms_int_div_by_3.add(current_num)

    return [len(all_perms_int_div_by_3), max(all_perms_int_div_by_3)]

print(find_mult_3(362))
print(find_mult_3(6063))



'''
from itertools import permutations

def find_mult_3(num):
  ls = []
  for i in range(1, len(str(num))+1):
    for j in set(permutations(str(num), i)):
      ls.append(int(''.join(j)))
  ls = set(ls)
  solve = [x for x in ls if x != 0 and x % 3 == 0]
  return [len(solve), max(solve)]
'''

'''
def find_mult_3(num):
    total = 0
    _max  = float("-inf")
    
    for lst in get_combos(num):    
        for i in lst:
            if i[0] != "0":
                number = int("".join(i))
                if number % 3 == 0:
                    total += 1
                    if number > _max:
                        _max = number
    return [total, _max]
    
def get_combos(num):
    return [set(itertools.permutations(str(num), i)) for i in range(1, len(str(num))+1)]
'''