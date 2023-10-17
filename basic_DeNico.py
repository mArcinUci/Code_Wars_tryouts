'''
description on: https://www.codewars.com/kata/596f610441372ee0de00006e/train/python
'''
massage = "2143658709"
key = "ba"
chunk_size = len(key)
ready_chunks = []
sorted_key = sorted(key)
new_order_in_chunks = [int(key.index(x)) for x in sorted_key]

def de_nico(key, msg):
    pass

def chunks(some_string, chunk_size):
    string_size = len(some_string)
    for x in range(0, string_size, chunk_size):
        yield some_string[x: min(x+chunk_size, string_size)]

for chunk in chunks(massage, chunk_size):
    new_chunk = ''.join(chunk[i] for i in new_order_in_chunks)
    ready_chunks.append(new_chunk)
ready_chunks = ''.join(ready_chunks)
print(ready_chunks)
# it works (for substr always equal to len(key)) but i cannot make it work when close it into function - look bellow:
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
deNico("crazy", "cseerntiofarmit on  ") => "secretinformation"
deNico("abc", "abcd") => "abcd"
deNico("ba", "2143658709") => "1234567890"
deNico("key", "eky") => "key" 
'''