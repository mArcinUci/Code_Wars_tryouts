'''Let's define a parameter of number n as the least common multiple (LCM) of the sum of its digits and their product.

Calculate the parameter of the given number n.'''


def parameter(n):
    new_n = str(n).strip()
    sum_of_digits_n = sum([int(x) for x in new_n])
    almost_product_of_digits_n = [int(x) for x in new_n]
    product_of_digits_n = 1
    for i in almost_product_of_digits_n:
        product_of_digits_n = product_of_digits_n * i

    for currentPossibleLCM in range(max(sum_of_digits_n,product_of_digits_n), (sum_of_digits_n*product_of_digits_n)+1):
         if((currentPossibleLCM % sum_of_digits_n == 0) and (currentPossibleLCM % product_of_digits_n == 0)):
              return currentPossibleLCM

print(parameter(1234))