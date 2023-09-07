'''How many strings equal to A can be constructed using letters from the string B? Each letter can be used only once and in one string only.'''



def strings_construction(a, b):
    how_many_letters_in_b = {}
    count = 0
    count_letters = 0
    for i in b:
        if i in how_many_letters_in_b:
            how_many_letters_in_b[i] += 1
        else:
            how_many_letters_in_b[i] = 1
    
    how_many_max_times_possible = len(b)//len(a)
    for i in range(how_many_max_times_possible):
        for x in a:
            if x in how_many_letters_in_b.keys() and how_many_letters_in_b[x] > 0:
                how_many_letters_in_b[x] -= 1
                count_letters += 1
            if count_letters == len(a):
                count += 1
    return count


print(strings_construction('abcd','cbadeabc'))