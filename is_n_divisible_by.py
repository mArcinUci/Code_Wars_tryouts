'''Create a function that checks if the first argument n is divisible by all other arguments (return true if no other arguments)'''

def is_divisible(*digits):
    main_digit = digits[0]
    count = 0
    len_digits = len(digits)
    for digit in digits:
        if main_digit % digit == 0:
            count += 1
    if count == len_digits:
        return True
    else:
        return False
    

print(is_divisible(12,6,3,2))