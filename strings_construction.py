'''How many strings equal to A can be constructed using letters from the string B? Each letter can be used only once and in one string only.'''



def strings_construction(a, b):
    how_many_letters_in_b = {}
    how_many_each_letters = []
    how_many_letters_occurance_in_a = []
    letters_in_a = []

    for i in b:
        if i in how_many_letters_in_b:
            how_many_letters_in_b[i] += 1
        else:
            how_many_letters_in_b[i] = 1
  
    for x in a:
        if x in how_many_letters_in_b.keys():
            how_many_each_letters.append(how_many_letters_in_b[x])
            if x not in letters_in_a:
                letters_in_a.append(x)
                how_many_letters_occurance_in_a.append(a.count(x))
        else:
            return 0
  
    how_many_each_letters_finally = list(map(lambda x,y: x//y, how_many_each_letters, how_many_letters_occurance_in_a))#list(map(lambda x, y: x * y, list1, list2))        
    if min(how_many_each_letters_finally) > len(b)//len(a): 
        return len(b)//len(a)
    else:
        return min(how_many_each_letters_finally)


print(f"should equal 1, and it shows {strings_construction('nbrbczc','cnrbbzccrbncbrn')}")
print(f"should equal 4, and it shows {strings_construction('qfhggrf' ,'gffhgffqfgffgrwrffqgqgghrufgqfhorgffggghghqhhuhqfq')}")