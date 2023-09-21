'''Just like in the "father" kata, you will have to return the last digit of the nth element in the Fibonacci sequence 
(starting with 1,1, to be extra clear, not with 0,1 or other numbers).
You will just get much bigger numbers, so good luck bruteforcing your way through it ;)'''


def last_fib_digit():
    x1 = 1
    x2 = 1
    def get_next_number():
        nonlocal x1, x2
        x3 = x1 + x2
        x1, x2 = x2, x3
        return x3
    return get_next_number


fibonacci = last_fib_digit()
for i in range(2, 50004):
    num = fibonacci()
print(num)
