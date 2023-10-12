'''
You have been speeding on a motorway and a police car had to stop you. The policeman is a funny guy that likes to play games.
Before issuing penalty charge notice he gives you a choice to change your penalty.
Your penalty charge is a combination of numbers like: speed of your car, speed limit in the area, speed of the police car chasing you,
 the number of police cars involved, etc. So, your task is to combine the given numbers and make the penalty charge to be as small as possible.
For example, if you are given numbers [45, 30, 50, 1] your best choice is 1304550
'''

from itertools import permutations

def penalty(a_list):
    
    tuples_of_all_premutations = list(permutations(a_list))
    list_of_all_permutations = [list(x) for x in tuples_of_all_premutations]
    final_list_of_all_permutations = [int("".join(map(str, x))) for x in list_of_all_permutations]
    min_penalty = str(min(final_list_of_all_permutations))
    
    return min_penalty

print(penalty(['45', '30', '50', '1']))  # 1304550 
print(penalty(['100', '10', '1']))       # 100101
print(penalty(['71', '82', '42', '34', '90']))  # 3442718290
print(penalty(['31', '97', '6', '78']))  # 3167897