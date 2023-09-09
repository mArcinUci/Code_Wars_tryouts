'''How many strings equal to A can be constructed using letters from the string B? Each letter can be used only once and in one string only.'''

def strings_construction(a, b):
    how_many_letters_in_b = {}
    how_many_each_letters = []
    how_many_letters_occurance_in_a = []

    for i in b:
        if i in how_many_letters_in_b:
            how_many_letters_in_b[i] += 1
        else:
            how_many_letters_in_b[i] = 1
    for x in set(a):
        if x in how_many_letters_in_b.keys():
            how_many_each_letters.append(how_many_letters_in_b[x])
            how_many_letters_occurance_in_a.append(a.count(x))
        else:
            return 0       
    how_many_each_letters_finally = [item1 // item2 for item1, item2 in zip(how_many_each_letters, how_many_letters_occurance_in_a)]
   
    return min(how_many_each_letters_finally)
    
    

print(f"should equal 1, and it shows {strings_construction('nbrbczc','cnrbbzccrbncbrn')}")
print(f"should equal 4, and it shows {strings_construction('qfhggrf' ,'gffhgffqfgffgrwrffqgqgghrufgqfhorgffggghghqhhuhqfq')}")


'''def strings_construction(A,B):
    return min(B.count(i)//A.count(i) for i in set(A))'''