'''Write a function that accepts a string, and returns the same string with all even indexed characters in each word upper cased,
 and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even,
   therefore that character should be upper cased and you need to start over for each word.
The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple
 words. Words will be separated by a single space(' ').'''

def to_weird_case(words):
    WiReD_StR = ''
    switch = 'big'
    for word in words:
        if switch == 'big':
            WiReD_StR += word.upper()
            switch = 'small'
        elif switch == 'small':
            WiReD_StR += word.lower()
            switch = 'big'
        if word.isspace():
            switch = 'big'
    return WiReD_StR
print(to_weird_case('ThIsa iS A TeSt i would liker to passe'))

'''def to_weird_case(string):
    recase = lambda s: "".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])
    return " ".join([recase(word) for word in string.split(" ")])'''