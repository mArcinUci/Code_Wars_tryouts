'''Start with the first number on the left then remove every other number moving right until you reach the the end,
 then from the numbers remaining start with the first number on the right and remove every other number moving left,
   repeat the process alternating between left and right until only one number remains which you return as the "last man standing"
'''


def last_man_standing(n):
    all_digits = [x for x in range(n+1)]
    count = 0
    print(all_digits)
    if len(all_digits) == 2:
        return all_digits
    while len(all_digits) > 2:
        next_element = all_digits[1]
        all_digits = all_digits[1:]
        all_digits = [x for x in all_digits if all_digits.index(x)%2 != all_digits.index(next_element)]
        count +=1
        print(f"cut from begining ------------->{all_digits}")
        if len(all_digits) >2:
            last_element = all_digits[-1]
            if len(all_digits)%2 == 0:
                all_digits = [x for x in all_digits if not all_digits.index(x)%2 == all_digits.index(last_element)%2]
                all_digits = all_digits[1:]
                count+=1
            else:
                all_digits = [x for x in all_digits if not all_digits.index(x)%2 == all_digits.index(last_element)%2]
                count+=1
            print(f"cut from end========>{all_digits}")
    if count%2==1:
        return all_digits[0]
    else:
        return all_digits[1]

print(last_man_standing(9))