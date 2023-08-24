def greatest_common_divisor(a,b):
    result = min(a,b)

    while result:
        if a % result == 0 and b % result == 0:
            break
        result -= 1
    
    return result

print(greatest_common_divisor(98,56))