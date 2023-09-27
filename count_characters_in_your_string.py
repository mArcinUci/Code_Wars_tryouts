'''
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
What if the string is empty? Then the result should be empty object literal, {}.
'''


def count(s):
    answer = {}

    for i in s:
        if i in answer:
            answer[i] += 1
        else:
            answer[i] = 1

    return answer

print(count('aba'))


'''
def count(string):
    return {i: string.count(i) for i in string}
'''

'''
def count(s):
    return {x:s.count(x) for x in set(s)}
'''