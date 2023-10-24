'''
Consider the following expansion:

solve("3(ab)") = "ababab"     -- because "ab" repeats 3 times
solve("2(a3(b))") = "abbbabbb" -- because "a3(b)" == "abbb", which repeats twice.

Given a string, return the expansion of that string.
Input will consist of only lowercase letters and numbers (1 to 9) in valid parenthesis. There will be no letters or numbers after 
the last closing parenthesis.
'''

from icecream import ic

def solve(st):
    solution = ''
    digits = ['0','1','2','3','4','5','6','7','8','9']
    bracket =  ['(', ')']
    for i in range(len(st)-1):
        if st[i] in digits:
            solution += f'{st[i]}*'   
        elif st[i] not in digits and st[i+1] in bracket  or st[i] == '(':
            solution += st[i]
        elif st[i] not in digits and st[i] not in bracket and st[i+1] not in bracket:
            solution += f'{st[i]}+'
    solution += ')'
   
    print(solution)
 
solve('2(a3(b))')
solve('k(a3(b(a2(c))))')
solve("3(b(2(c)))")

        

x = 2*('a'+3*('b')) #<----- "2(a3(b))"
y = 'k'+('a'+ 3*('b'+('a'+2*'c'))) # <---- "k(a3(b(a2(c))))"
#  "2(a3(b))" ---> "abbbabbb"
#  "k(a3(b(a2(c))))" ---> "kabaccbaccbacc"