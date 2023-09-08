'''How many strings equal to A can be constructed using letters from the string B? Each letter can be used only once and in one string only.'''



def strings_construction(a, b):
    how_many_letters_in_b = {}
    how_many_each_letters = []
    for i in b:
        if i in how_many_letters_in_b:
            how_many_letters_in_b[i] += 1
        else:
            how_many_letters_in_b[i] = 1
    print(how_many_letters_in_b) 
    print(how_many_each_letters)
    print(len(b)/len(a))

    for x in a:
        if x in how_many_letters_in_b.keys():
            how_many_each_letters.append(how_many_letters_in_b[x])
        else:
            return 0
              
    if min(how_many_each_letters) > len(b)//len(a):
        return len(b)//len(a)
    else:
        return min(how_many_each_letters)


print(strings_construction("hnuqnpowym",'pzqwpqhmupmwmbymywumpnkwuqjoum'))
# so n is only 1 in b but 2 times in a, how to count that
print(strings_construction("nlheprlp",'hheeppeerlpplherhnnlrhlrprpppellprnlnprrhlnrppnllh'))