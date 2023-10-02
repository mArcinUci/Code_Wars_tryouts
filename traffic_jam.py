def traffic_jam(main_road, side_streets):
    final_line = []
    the_main_road = []
    pointer = 'X'
    for x in range(len(main_road)):
        if main_road[x] is not pointer:
            the_main_road.append(['-',main_road[x]])
        else:
            the_main_road.append(pointer)
   
    while the_main_road[0] is not pointer:
        final_line.append(the_main_road[0])
        the_main_road = the_main_road[1:]
        for i in range(len(side_streets)):
            if i == 0 and len(side_streets[0])>0 and side_streets[0][0] != final_line[-1]:
               the_main_road = [side_streets[0][0]] + the_main_road
               side_streets[i] = side_streets[0][1:]               
               break
            elif i>0 and len(side_streets[i])>0 and side_streets[i][0] != the_main_road[i-1]:
               the_main_road = the_main_road[:i] + [str(side_streets[i][0])] + the_main_road[i:]
               side_streets[i] = side_streets[i][1:]
               break
  
    for x in range(len(final_line)):
        if len(final_line[x]) > 1:
            final_line[x] = final_line[x][1]
  
    final_line.append('X')
    final_line = ''.join(final_line)
    return final_line

      
#to pass all tests I need to differentiate beetween main and side streets (it is not always so main is lower and side is upper) 

print(traffic_jam("abcdefX", []), "abcdefX")
print(traffic_jam("abcXdef", []), "abcX")
print(traffic_jam("Xabcdef", []), "X")
print(traffic_jam("abcdefghijklmX", ["","","","BBBBBB","","","","","CCCCC"]), "abcdBeBfBgBhBiBCjCkClCmCX")
print(traffic_jam("abcdeXghi", ["","","CCCCC","","EEEEEEEEEE","FFFFFF","","","IIIIII"]), "abcCdCeCECX")
#print(traffic_jam("abcdefghijklmX", ["","","","BBBBBB","","","","","CCCCC"]), "abcdBeBfBgBhBiBCjCkClCmCX")


#traffic_jam("abcdefghijklmnopqrstuvwX", ["AAA","BBB","CCC", "DDD","EEE", "FFF", "GGG", "HHH", "III", "JJJ", "KKK", "LLL", "MMM", "NNN", "OOO", "PPP", "QQQ", "RRR", "SSS", "TTT", "UUU", "VVV", "WWW"])