'''description on: https://www.codewars.com/kata/5b5f7f7607a266914200007c/train/python'''

from icecream import ic
from itertools import combinations

def combs_non_empty_boxes(n,k):
    if k > n:
        return "It cannot be possible!"
    if k == 0:
        return 0
    
    
    
    


print(combs_non_empty_boxes(4,3)) #15170932662679