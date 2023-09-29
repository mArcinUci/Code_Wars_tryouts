def traffic_jam(main_road, side_streets):
    final_line = []
    pointer = 'X'
    while main_road[0] is not pointer:
        final_line.append(main_road[0])
        main_road = main_road[1:]
        for i in range(len(side_streets)):
            if len(side_streets[i])>0 and side_streets[i][0] != main_road[i-1]:
                main_road = main_road[:i] + str(side_streets[i][0]) + main_road[i:]
                side_streets[i] = side_streets[i][1:]
                break

    final_line.append('X')
    final_line = ''.join(final_line)
    return final_line

      
#problem with situation when first side street (index 0) is occupied  

print(traffic_jam("abcdefX", []), "abcdefX")
print(traffic_jam("abcXdef", []), "abcX")
print(traffic_jam("Xabcdef", []), "X")
print(traffic_jam("abcdefghijklmX", ["","","","BBBBBB","","","","","CCCCC"]))
print(traffic_jam("abcdeXghi", ["","","CCCCC","","EEEEEEEEEE","FFFFFF","","","IIIIII"]))
print(traffic_jam("abcdefghijklmX", ["","","","BBBBBB","","","","","CCCCC"]), "abcdBeBfBgBhBiBCjCkClCmCX")
print(traffic_jam("abcdeXghi", ["","","CCCCC","","EEEEEEEEEE","FFFFFF","","","IIIIII"]), "abcCdCeCECX")
print(traffic_jam("abcdefghijklmX", ["","","","BBBBBB","","","","","CCCCC"]), "abcdBeBfBgBhBiBCjCkClCmCX")