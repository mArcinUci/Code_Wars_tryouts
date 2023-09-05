'''it is to long to copy description, so: https://www.codewars.com/kata/55b4d87a3766d9873a0000d4/train/python'''


def howmuch(m, n):
    answer = []
    amount_of_money = 0
    if m >= n:
        amount_of_money = [x for x in range(n,m+1)]
    else:
        amount_of_money = [x for x in range(m, n+1)]
    
    for i in amount_of_money:
        if i % 7 == 2 and i % 9 == 1:
            answer.append([f'M: {i}', f'B: {i//7}', f'C: {i//9}'])
    return answer

print(howmuch(1,100))


'''def howmuch(m, n):
    i = min(m, n)
    j = max(m, n)
    res = []
    while (i <= j):
        if ((i % 9 == 1) and (i %7 == 2)):
            res.append(["M: " + str(i), "B: " + str(i // 7), "C: " + str(i // 9)])
        i += 1
    return res'''