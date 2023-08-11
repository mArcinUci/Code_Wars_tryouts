'''In this kata you'll be given a number n >= 2 and output a list with all positive integers less than gcd(n, k) == 1, 
with k being any of the output numbers.
The list cannot include duplicated entries and has to be sorted.'''



def coprimes(n):
    list_of_numbers = [x for x in range(1,n) if n%x != 0]
    list_of_coprimes = [1]
    for i in list_of_numbers:
        result = i
        while result:
            if i % result != 0 and n % result !=0:
                list_of_coprimes.append(result)
            result -= 1
        


    return list_of_coprimes

print(coprimes(6))