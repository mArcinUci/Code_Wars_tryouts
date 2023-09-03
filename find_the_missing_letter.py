'''Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.
You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2. The array will always contain letters in only one case.'''

def find_missing_letter(chars):
    for i in range(len(chars)):
        if ord(chars[i])+1 != ord(chars[i+1]):
            return chr(ord(chars[i])+1)

print(find_missing_letter(['a','b','c','d','f']))


'''def find_missing_letter(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n+1]) - 1:
        n += 1
    return chr(1+ord(chars[n]))'''