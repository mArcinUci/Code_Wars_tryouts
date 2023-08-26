'''Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings.
Consonants are any letters of the alphabet except "aeiou".
We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.
For example, for the word "zodiacs", let's cross out the vowels. We get: "z o d ia cs"'''

def solve(s):
    s = list(s)
    bad_letters = 'aeiou'
    alphabet = ' abcdefghijklmnopqrstuvwxyz'
    letters_position = []
    ans =''
    answer = []
    score = 0
    for i in s:
        if i in bad_letters:
            s[s.index(i)] = ' '
    odp = ans.join(s)
    
    for i in odp.lower():
        if i in alphabet:
            letters_position.append(alphabet.index(i))
    
    letters_position.append(0)
    for i in letters_position:
        score += i
        if i == 0:
            answer.append(score)
            score = 0

    return max(answer)



print(solve('cozy'))





#different solutions
'''def solve(s):
    alphabet = "-abcdefghijklmnopqrstuvwxyz"
    for vowel in "aeiou":
        s = s.replace(vowel, " ")
    values = []
    for item in s.split():
        sum = 0
        for letter in item:
            sum += alphabet.index(letter)
        values.append(sum)        
    return max(values)'''

#or 
'''def solve(s):
    a = [s:=s.replace(x,' ') for x in 'aeiou'][-1].split()'''