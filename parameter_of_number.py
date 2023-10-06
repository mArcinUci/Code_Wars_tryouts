'''Let's define a parameter of number n as the least common multiple (LCM) of the sum of its digits and their product.

Calculate the parameter of the given number n.'''


import math

def parameter(n):
    def lcm(x, y):
        return abs(x * y) // math.gcd(x, y) if x and y else 0

    digits = [int(digit) for digit in str(n)]
    sum_of_digits = sum(digits)
    product_of_digits = math.prod(digits)

    return lcm(sum_of_digits, product_of_digits)






#my old solution (or more training example)
'''
def parameter(n):
    new_n = str(n).strip()
    sum_of_digits_n = sum([int(x) for x in new_n])
    almost_product_of_digits_n = [int(x) for x in new_n]
    product_of_digits_n = 1
    for i in almost_product_of_digits_n:
        product_of_digits_n = product_of_digits_n * i

    
    if sum_of_digits_n > product_of_digits_n:
        greater = sum_of_digits_n
    else:
        greater = product_of_digits_n

    while True:
        if greater % sum_of_digits_n == 0 and greater % product_of_digits_n == 0:
            least_common_multiple = greater
            break   
        greater += 1    
    
    yield least_common_multiple
'''

#others solutions

'''
from math import gcd

def parameter(n):
    s, p = 0, 1
    for m in str(n):
        s += int(m)
        p *= int(m)
    return (s * p / (gcd(s, p)))
'''


'''
def parameter(n):
    n = [int(digit) for digit in str(n)]
    lcm_1 = sum(n)
    lcm_2 = 1
    for i in n:
        lcm_2 *= i
    
    gdc_1 = lcm_1
    gdc_2 = lcm_2
    
    while gdc_2 != 0:
        gdc_1, gdc_2 = gdc_2, gdc_1 % gdc_2
    gdc = gdc_1

    lcm = (lcm_1 * lcm_2) / gdc
    return lcm
'''


'''
def lcm(a, b):
    maximum = max(a, b)
    minimum = min(a, b)
    res = maximum
    while res % minimum:
        res += maximum
    return res

def parameter(n):
    sum = 0
    prod = 1
    for char in str(n):
        sum += int(char)
        prod *= int(char)
    return lcm(sum, prod)
'''