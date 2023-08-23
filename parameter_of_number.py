'''Let's define a parameter of number n as the least common multiple (LCM) of the sum of its digits and their product.

Calculate the parameter of the given number n.'''


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
    return least_common_multiple


print(parameter(22))