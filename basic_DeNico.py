'''
description on: https://www.codewars.com/kata/596f610441372ee0de00006e/train/python
'''
from icecream import ic 

def de_nico(key, message):
    not_ready_chunks = []
    ready_chunks = []
    chunk_size = len(key)
    string_size = len(message)
    char_positions = {char: i for i, char in enumerate(sorted(key))}
    original_order_in_chunks = [char_positions[char] for char in key]
    
    for x in range(0, string_size, chunk_size):
        not_ready_chunks.append(message[x: min(x + chunk_size, string_size)])

    for chunk in not_ready_chunks:
        new_chunk = ''.join(chunk[i] for i in original_order_in_chunks if i < len(chunk))
        ready_chunks.append(new_chunk)

    result = ''.join(ready_chunks)
    return result.rstrip()


print(de_nico("crazy", "cseerntiofarmit on "))
print(de_nico("abc", "abc"))
print(de_nico("ba", "2143658709"))
print(de_nico("key", "eky"))


#som others creative ideas (from CodeWars)

'''
def de_nico(key, msg):
    ll, order, s = len(key), [sorted(key).index(c) for c in key], ''
    while msg:
        s, msg = s + ''.join(msg[i] for i in order if i < len(msg)), msg[ll:]
    return s.strip()
'''


'''
def de_nico(key,msg):
    result = ''
    counter = -1
    while len(result) < len(msg):
        counter += 1
        for i in [sorted(key).index(c) for c in key]:
            try:
                result += msg[i+counter*len(key)]
            except:
                continue
    return result.strip()
'''


#my previous tryouts
'''
def de_nico(key, massage):
    
    not_ready_chunks = []
    ready_chunks = []
    chunk_size = len(key)
    string_size = len(massage)
    sorted_key = sorted(key)
    print(sorted_key)
    new_order_in_chunks = [int(key.index(x)) for x in sorted_key]
    print(new_order_in_chunks)
    for x in range(0, string_size, chunk_size):
        not_ready_chunks.append(massage[x: min(x+chunk_size, string_size)])
    for chunk in not_ready_chunks:
        new_chunk =  ' '.join(''.join(s[i] for i in new_order_in_chunks if i < len(s)) for s in chunk) #[''.join(s[i] for i in new_order_in_chunks if i < len(s)) for s in chunk]
        ready_chunks.append(new_chunk)
    ready_chunks = ''.join(''.join(word.split()) for word in ready_chunks)
    return ready_chunks
'''


'''
def de_nico(key, some_string):

    chunk_size = len(key)
    string_size = len(some_string)
    for x in range(0, string_size, chunk_size):
        yield some_string[x: min(x+chunk_size, string_size)]

    ready_chunks = []
    chunk_size = len(key)
    sorted_key = sorted(key)
    new_order_in_chunks = [int(key.index(x)) for x in sorted_key]

    for chunk in de_nico(some_string, chunk_size): 
        chunk = ''.join(chunk[i] for i in new_order_in_chunks)
        ready_chunks.append(chunk)
        print(ready_chunks)
    return list(ready_chunks)

print(de_nico('niko', '123412341234'))
'''



'''
Examples:
de_nico("crazy", "cseerntiofarmit on  ") => "secretinformation"
de_nico("abc", "abcd") => "abcd"
de_nico("ba", "2143658709") => "1234567890"
de_nico("key", "eky") => "key" 
'''