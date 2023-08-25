'''In this kata you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
"a" = 1, "b" = 2, etc.'''



def alphabet_position(text):
    alphabet = ' abcdefghijklmnopqrstuvwxyz'
    letters_position = []
    answer = ''
    for i in text.lower():
        if i in alphabet:
            letters_position.append(alphabet.index(i))
    #letters_position.reverse()    
    for i in letters_position:
        answer += str(i)
        answer += ' '

    return answer.strip()
print(alphabet_position("TkZaYoxZefLUtChoaDqJDHuDTxMLeYwwMvnxNFkOGJnovaorYHpRNTbTXHtaNlvZxXXYMnEmDRWfyleCoAEAKcrcmCoaPyvCajLl"))




# "TkZaYoxZefLUtChoaDqJDHuDTxMLeYwwMvnxNFkOGJnovaorYHpRNTbTXHtaNlvZxXXYMnEmDRWfyleCoAEAKcrcmCoaPyvCajLl"
#  '20 11 26 1 25 15 24 26 5 6 12 21 20 3 8 15 1 4 17 10 4 8 21 4 20 24 13 12 5 25 23 23 13 22 14 24 14 6 
# 11 15 7 10 14 15 22 1 15 18 25 8 16 18 14 20 2 20 24 8 20 1 14 12 22 26 24 24 24 25 13 14 5 13 4 18 23 6 
# 25 12 5 3 15 1 5 1 11 3 18 3 13 3 15 1 16 25 22 3 1 10 12 12'