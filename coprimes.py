'''In this kata you'll be given a number n >= 2 and output a list with all positive integers less than gcd(n, k) == 1, 
with k being any of the output numbers.
The list cannot include duplicated entries and has to be sorted.'''



def coprimes(n):
    list_of_coprimes = [x for x in range(1,n) if n%x != 0]
    list_of_codivisibles = []
    for num in list_of_coprimes:
        dummy = num
        while dummy-1:
            if n%dummy == 0 and num%dummy==0:
                list_of_codivisibles.append(num)
                break
            dummy -= 1    
    list_of_coprimes.append(1)

    final_list_of_coprimes = [x for x in list_of_coprimes if x not in list_of_codivisibles]
    return sorted(final_list_of_coprimes)
   
print(coprimes(10))