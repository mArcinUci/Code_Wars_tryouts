'''Create a function that takes a list of integers and a group length as parameters. Your task is to determine if it's possible to 
split all the numbers from the list into groups of the specified length, while ensuring that consecutive numbers are present within 
each group.'''


def consecutive_nums(lst, group_len):
    if group_len == 1:
        return True
    lst_len = len(lst)
    if lst_len % group_len != 0:
        return False
    else:
        lst = sorted(lst)
        pass
            
                       
        
    

print(consecutive_nums([1, 3, 5], 1))


# I do not get why this one is True:  consecutive_nums([1, 3, 5], 1), True)   (consecutive_nums([5, 6, 3, 4], 2), True
# and why this one is False  consecutive_nums([1, 3, 4, 5], 2), False

#and it do not pass this example    (consecutive_nums([1, 2, 3, 3, 3, 3], 3) -->should be: False


# solution ????:    https://www.geeksforgeeks.org/check-if-an-array-can-be-split-into-subsets-of-k-consecutive-elements/