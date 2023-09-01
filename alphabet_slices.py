def solutions(s):
    dummy = None
    for i in range(len(s)-1):
        if ord(s[i])+1 == ord(s[i+1]):
            if dummy is None:
                dummy = i
        elif dummy is not None:
            slice = s[dummy:i+1]
            reversed_slice = slice[::-1]
            s = s[:dummy] + reversed_slice + s[i+1:]
            dummy = None
    if dummy is not None:
        last_slice = s[dummy:]
        last_reversed_slice = last_slice[::-1]
        s = s[:dummy]+last_reversed_slice
        
    return s
print(solutions('ggabcggabcffbcdxyz'))
