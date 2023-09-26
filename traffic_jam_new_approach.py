def traffic_jam(main_road, side_streets):
    last_line = []
    pointer = ''

    for i in side_streets:
        main_pointer_index = side_streets.index(i)
        if len(i)>0:
            last_line = main_road[:main_pointer_index]
            main_road = main_road[:main_pointer_index]
            break
    
    while pointer != 'X':
        last_line.append(main_road[0])
        main_road = main_road[1:]
        pointer = str(main_road[0])
        for i in side_streets:
            if len(i) > 0 and i[0] != last_line[-1]:
                last_line.append(i[0])
                pointer = i[0]
                i.pop[-1]
                print(i)
                break
    
        
#problem with stings and lists --> when trying to solve it that way  
    
print(traffic_jam("abcdefghijklmX",  ["","","","BBBBBB","","","","","CCCCC"] ))

