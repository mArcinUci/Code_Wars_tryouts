'''Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.'''
'''pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !'''

def pig_it(text):
    text = text.split()
    new_text = []
    for i in text:
        new_word = i[1:]+i[0]+'ay'
        if i not in ['?','!']:
            new_text.append(new_word)
        if i in ['?','!']:
            new_text.append(i)
    new_text = ' '.join(new_text)
    return new_text
print(pig_it('O tempora o mores !'))



'''new_text = ' '.join([(x[1:]+x[0]+'ay') if x.isalpha() else x for x in text ])'''