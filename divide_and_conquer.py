'''Create a function that takes a list of integers and a group length as parameters. Your task is to determine if it's possible to 
split all the numbers from the list into groups of the specified length, while ensuring that consecutive numbers are present within 
each group.'''

from collections import defaultdict

def consecutive_nums(lst, group_len):
    
    sorted_lst = sorted(lst)
    all_digits_dict = defaultdict(int)
    count = 0
    

    for i in sorted_lst:
        all_digits_dict[i] += 1
  
    
    for x in range(group_len):
        for key,value in all_digits_dict.items():
            if key + x in all_digits_dict and all_digits_dict[key+x]>0:
                all_digits_dict[key+x] -= 1
                count += 1
    if count == len(sorted_lst):
        return True
    else:
        return False
         
            







print(consecutive_nums([1, 2, 3, 3, 2, 3, 4, 7, 8], 3))   
print(consecutive_nums([5, 5, 7, 3, 3, 1, 1, 1, 2, 6, 6, 7, 2, 2, 3], 3))
print(consecutive_nums([1, 3, 4, 5], 2))
print(consecutive_nums([1, 2, 3, 3, 3, 3], 3))
#True
#False  
#False
#False


#(consecutive_nums([5, 5, 7, 3, 3, 1, 1, 1, 2, 6, 6, 7, 2, 2, 3], 3), True)

