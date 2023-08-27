'''Write a function revSub which reverses all sublists where consecutive elements are even.
 Note that the odd numbers should remain where they are.'''



'''def rev_sub(arr):
    count = len(arr)
    dummy = 0
    while dummy<count:
        if arr[dummy] % 2 == 1:
            slice_1_arr = arr[:dummy]
            slice_2_arr = arr[dummy:]
            print(slice_1_arr)
            print(slice_2_arr)
            new_slice_arr = slice_1_arr[::-1]
            print(new_slice_arr)
            arr = new_slice_arr + slice_2_arr
        dummy += 1

    return arr


print(rev_sub([2, 4, 3, 2,10,1]))'''

def reverse_even_sequences(lst):
    start = None
    length = len(lst)

    for i in range(length):
        if lst[i] % 2 == 0:
            if start is None:
                start = i
        elif start is not None:
            sublist = lst[start:i]
            lst[start:i] = sublist[::-1]
            start = None

    if start is not None:  # Reverse the last sequence if it's even
        sublist = lst[start:]
        lst[start:] = sublist[::-1]

    return lst

# Example usage
numbers = [3, 6, 8, 10, 12, 5, 7, 9, 14, 16, 18, 20]
result = reverse_even_sequences(numbers)
print(result)