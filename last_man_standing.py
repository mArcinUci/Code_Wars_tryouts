'''Start with the first number on the left then remove every other number moving right until you reach the the end,
 then from the numbers remaining start with the first number on the right and remove every other number moving left,
   repeat the process alternating between left and right until only one number remains which you return as the "last man standing"
'''


def last_man_standing(n):
    all_digits = [x for x in range(1,n+1)]
    print(all_digits)
    while len(all_digits) > 1:
        all_digits = all_digits[1::2]
        print(all_digits)
        if len(all_digits)>1:
            all_digits = all_digits[::-1]
            print(all_digits)
            all_digits = all_digits[1::2]
            print(all_digits)
            all_digits = all_digits[::-1]
            print(all_digits)

    return all_digits

        


print(last_man_standing(1000))