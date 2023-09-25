'''Just like in the "father" kata, you will have to return the last digit of the nth element in the Fibonacci sequence 
(starting with 1,1, to be extra clear, not with 0,1 or other numbers).
You will just get much bigger numbers, so good luck bruteforcing your way through it ;)'''


def fibo(n):
    f1, f2 = 0, 1
    for _ in range(n-1):
        f1, f2 = f2, (f1+f2)%10
    return f2

print(fibo(80000007))



'''
def fib_digit(n):
    f=[1,1]
    for i in range(2,n):
        f.append((f[i-1]+f[i-2])  % 10 ) 
    return f[-1]

print(fib_digit(80000007))
'''

'''
# the Pell's equation to p and q
import math
 
p = (1 + math.sqrt(5)) / 2
q = (1 - math.sqrt(5)) / 2
 
def fib(n):
    i = n - 1
    x = (p**i - q**i) / (p - q)
    return int(x)

print(fib(80000007))  # OverflowError: (34, 'Result too large')
'''


'''
# it`s not my math level, and suposed to bo O(1) formula, it does not count properly
import math
def fi(n):
    log_d = math.log(-(1 - math.sqrt(5))/(1 + math.sqrt(5)))
    sign = -1 if n % 2 else 1
    return math.log(1 / math.sqrt(5)) + n*math.log((1 + math.sqrt(5)) / 2) + math.log(1 - sign * math.exp(n * log_d))


print(fi(302)) # proper -> 1  gives 144.5212522117832
print(fi(80000007)) # proper 8   gives  38496948.568532094
print(fi(900000008)) # proper 1    gives  433090645.59861875
print(fi(1000000009)) # proper 9     gives  481211828.58579093
'''
'''
import math
def fibona(n):
    x = (math.sqrt(5)+1)/2
    num = round(math.pow(x,n)/math.sqrt(5))
    return num

print(fibona(302))
print(fibona(50004)) # OverflowError: math range error
'''







'''
def last_fib_digit():
    x1 = 1
    x2 = 1
    def get_next_number():
        nonlocal x1, x2
        x3 = x1 + x2
        x1, x2 = x2, x3
        return x3
    return get_next_number

answer = ''
fibonacci = last_fib_digit()
for i in range(2, 50004):
    num = fibonacci()
answer += str(num)
new_ans = answer[-1]
print(int(new_ans))
'''




'''
# cannot install library, seemed to be promising one

from sympy import fibonacci
fibonacci(7000006)
'''


'''
def fibonacci(digits) :
    a,b,n = 1,1,2
    while len(str(b)) < digits :
        a, b, n = b, b+a, n+1
    yield n

gen_fib = fibonacci(50004) 
print(gen_fib)
'''

'''
#it doesn`t work either

def last_fib_digit(n):
    x, y = 1, 1
    for _ in range(n):
        x, y = y, x + y
    answer = ''
    answer += str(x)
    last_digit = answer[-1]
    return int(last_digit)
'''

'''
def fibonacci(digits) :
    a,b,n = 1,1,2
    while len(str(b)) < digits :
        a, b, n = b, b+a, n+1
    return n
'''

'''
def fib(n):
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    ans = str(v2)
    return int(ans[-1])
print(fib(7000006))
'''