'''Create a function that takes a list of integers and a group length as parameters. Your task is to determine if it's possible to 
split all the numbers from the list into groups of the specified length, while ensuring that consecutive numbers are present within 
each group.'''

from collections import defaultdict

def consecutive_nums(lst, group_len):
    ordered_dict = defaultdict(int)
    
    if group_len == 1:
        return True
    lst_len = len(lst)
    if lst_len % group_len != 0:
        return False
    else:
        lst = sorted(lst)
        for i in lst:
            ordered_dict[i] += 1

        for key,value in ordered_dict.items():
            dummy = key
            digit = value
            if digit > 0:
                for x in range(1,group_len):
                    if dummy + x not in ordered_dict:
                        return False
                    ordered_dict[dummy+x] -= 1
                    if ordered_dict[dummy+1] < 0:
                        return False
        return True
                               
print(consecutive_nums([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))   
print(consecutive_nums([5, 5, 7, 3, 3, 1, 1, 1, 2, 6, 6, 7, 2, 2, 3], 3))
print(consecutive_nums([1, 3, 4, 5], 2))
print(consecutive_nums([1, 2, 3, 3, 3, 3], 3))
#True
#False  (?????)
#False
#False

a = sorted([5, 5, 7, 3, 3, 1, 1, 1, 2, 6, 6, 7, 2, 2, 3])
#(consecutive_nums([5, 5, 7, 3, 3, 1, 1, 1, 2, 6, 6, 7, 2, 2, 3], 3), True)
print(a) #[1, 1, 1, 2, 2, 2, 3, 3, 3, 5, 5, 6, 6, 7, 7]  ======> I do not know how it suposed to work??? or maybe I do not understand task??

# I do not get why this one is True:  consecutive_nums([1, 3, 5], 1), True)   (consecutive_nums([5, 6, 3, 4], 2), True
# and why this one is False  consecutive_nums([1, 3, 4, 5], 2), False