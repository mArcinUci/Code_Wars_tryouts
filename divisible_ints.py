'''You are given an integer N. Your job is to figure out how many substrings inside of N divide evenly with N'''


def get_count(n):
    n = str(n)
    all_possible_substrings_from_n = [n[i:j] for i in range(len(n))
                                for j in range(i + 1, len(n) + 1)]
    all_possible_ints_from_n = [int(x) for x in all_possible_substrings_from_n if int(x) != 0]
    answer = 0
    for i in all_possible_ints_from_n:
        if int(n) % i == 0 and int(n) != i:
            answer +=1

    return answer

print(get_count(123))

