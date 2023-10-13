'''
You have been speeding on a motorway and a police car had to stop you. The policeman is a funny guy that likes to play games.
Before issuing penalty charge notice he gives you a choice to change your penalty.
Your penalty charge is a combination of numbers like: speed of your car, speed limit in the area, speed of the police car chasing you,
 the number of police cars involved, etc. So, your task is to combine the given numbers and make the penalty charge to be as small as possible.
For example, if you are given numbers [45, 30, 50, 1] your best choice is 1304550
'''

def penalty(a_list):
    lenght_list = [len(x) for x in a_list]
    uniq_lenght_list = list(set(lenght_list))
    common_product = 1
    for x in uniq_lenght_list:
        common_product = common_product * x
    product_for_every_item = [int(common_product/x) for x in lenght_list]
    final_list = [a*b for a,b in zip(a_list,product_for_every_item)]
    common_list = zip(final_list, a_list)
    common_list = sorted(common_list)
    min_penalty = ''
    for i in common_list:
        min_penalty += i[1]
    return min_penalty
    


print(penalty(['45', '30', '50', '1']))  # 1304550 
print(penalty(['100', '10', '1']))       # 100101
print(penalty(['71', '82', '42', '34', '90']))  # 3442718290
print(penalty(['31', '97', '6', '78']))  # 3167897

# my other (bigger time complexity) solution
'''
from itertools import permutations

def penalty(a_list):
    
    tuples_of_all_premutations = list(permutations(a_list))
    list_of_all_permutations = [list(x) for x in tuples_of_all_premutations]
    final_list_of_all_permutations = [int("".join(map(str, x))) for x in list_of_all_permutations]
    min_penalty = str(min(final_list_of_all_permutations))
    
    return min_penalty
'''

#solutions from CodeWars

'''
# return str of the smallest value of the combined numbers in a_list
# the length of a_list can vary betweem 2 and 20  
def penalty(a_list):
    return ''.join(sorted(a_list, key=lambda x: x+x))
'''


'''
# return str of the smallest value of the combined numbers in a_list
# the length of a_list can vary betweem 2 and 20  
def penalty(a_list):
    return ''.join(sorted(sorted(a_list, key=lambda x: x[-1]), key=lambda x: x[0]))
'''


'''
# return str of the smallest value of the combined numbers in a_list
# the length of a_list can vary betweem 2 and 20  
def val_num(x):
    suma =0
    for i, y in enumerate(x, start=1):
        suma += i*int(y)
    return x * 10 *len(x)
def penalty(a_list):
    print(sorted(a_list,key=lambda x: (val_num, len)))
    return "".join(sorted(a_list,key=val_num))
#     return "".join(sorted(a_list, key=lambda x: sum(ord(y) for y in x)))
'''