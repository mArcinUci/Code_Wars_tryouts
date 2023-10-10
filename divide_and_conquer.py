'''Create a function that takes a list of integers and a group length as parameters. Your task is to determine if it's possible to 
split all the numbers from the list into groups of the specified length, while ensuring that consecutive numbers are present within 
each group.'''


def consecutive_nums(lst, group_len):
    sorted_lst = sorted(lst)
    second_list = lst
    sublist = []
    operation_counter = 0
    print(f'sorted list before looks like: {sorted_lst}')
    bubble = int(len(second_list)/group_len + 1)
    while bubble:
        for i in sorted_lst:
            if len(sublist) == group_len or operation_counter == group_len:
                for x in sublist:
                    sorted_lst.remove(x)
                print(f'-------{sublist}-------')
                print(f'sorted list after looks like: {sorted_lst}')
                operation_counter = 0
                sublist = []
                break
            if len(sublist) == 0:
                sublist.append(i)
                operation_counter += 1
            if i == sublist[-1]+1:
                sublist.append(i)
                operation_counter += 1
        bubble -= 1
            
    if len(sorted_lst) == 0:
        return True
    else:
        return False  


print(consecutive_nums([1,3,4,2,6,7,9,10], 2))
print(consecutive_nums([1,3,4,2,6,7,9,10,45], 2))
print(consecutive_nums([1,2,8,9], 2)) 
print(consecutive_nums([1, 2, 3, 3, 2, 3, 4, 7, 8], 3))   
print(consecutive_nums([5, 5, 7, 3, 3, 1, 1, 1, 2, 6, 6, 7, 2, 2, 3], 3))
print(consecutive_nums([1, 3, 4, 5], 2))
print(consecutive_nums([1, 2, 3, 3, 3, 3], 3))
#True
#False  
#False
#False













'''
def consecutive_nums(lst, group_len):
    
    sorted_lst = sorted(lst)
    second_sorted_lst = sorted(lst)
    count = 0
    count_eee = 0
    sublist = []
    for _ in range(group_len):
        for i in sorted_lst:
            count_eee +=1
            if len(sublist) == 0:
                sublist.append(i)
                sorted_lst = sorted_lst[1:]   
            if i - 1 == sublist[-1]:
                sublist.append(i)
                sorted_lst = sorted_lst[1:]
            if len(sublist) == group_len:
                print(sublist)
                count += group_len
                sublist = []
            if count_eee == len(second_sorted_lst):
                count_eee = 0
                break 
                     
    if count == len(second_sorted_lst):
        return True
    else:
        print(count)

        return False
'''         
            

'''
from collections import defaultdict

 all_digits_dict = defaultdict(int)
for i in sorted_lst:
        all_digits_dict[i] += 1

for key,value in all_digits_dict.items():
            if key + x in all_digits_dict and all_digits_dict[key+x]>0:
                all_digits_dict[key+x] -= 1
'''

#print(consecutive_nums([1,2,8,9], 2)) 
#print(consecutive_nums([1, 2, 3, 3, 2, 3, 4, 7, 8], 3))   
#print(consecutive_nums([5, 5, 7, 3, 3, 1, 1, 1, 2, 6, 6, 7, 2, 2, 3], 3))
#print(consecutive_nums([1, 3, 4, 5], 2))
#print(consecutive_nums([1, 2, 3, 3, 3, 3], 3))
#True
#False  
#False
#False


#(consecutive_nums([5, 5, 7, 3, 3, 1, 1, 1, 2, 6, 6, 7, 2, 2, 3], 3), True)

