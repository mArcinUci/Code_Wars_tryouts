'''
description on: https://www.codewars.com/kata/596f610441372ee0de00006e/train/python
'''
massage = 'abcdefghijkl'
key = 'nico'
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
    new_chunk = chunk
    for i in new_order_in_chunks:
        print(f'-------{new_chunk[new_order_in_chunks.index(i)]}--------')
        print(chunk[i])    
        new_chunk.replace(new_chunk[new_order_in_chunks.index(i)], chunk[i])
        print(f'======={new_chunk}======')
        #new_chunk[new_order_in_chunks.index(i)] = chunk[i]
        break
    ready_chunks.append(new_chunk)


print(ready_chunks)


'''
my plan:
- rearrange key and according to that rearrange msg using len(msg) sublists
but my brain does not work today after all work i have don so far, i will try tommorow
'''







'''
Examples:
deNico("crazy", "cseerntiofarmit on  ") => "secretinformation"
deNico("abc", "abcd") => "abcd"
deNico("ba", "2143658709") => "1234567890"
deNico("key", "eky") => "key" 
'''