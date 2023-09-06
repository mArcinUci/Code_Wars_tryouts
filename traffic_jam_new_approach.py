def traffic_jam(main_road, side_streets):
    pointer = None
    whoose_turn = 'start procedure'
    sytuation_on_main_road = main_road
    sytuation_on_side_streets = side_streets

    final_line = []
    
    while pointer != 'X':
        if whoose_turn == 'start procedure':
            for i in side_streets:
                if len(i) > 0:
                    starting_pointer = side_streets.index(i)
                    break
            for i in range(starting_pointer+1):
                final_line.append(sytuation_on_main_road[i])
                pointer = i
            sytuation_on_main_road = sytuation_on_main_road[i+1:]
            whoose_turn = 'main'
                    

        if whoose_turn == 'main':
            print(final_line)
            print(sytuation_on_main_road[0])
            final_line.append(sytuation_on_main_road[0])
            pointer = sytuation_on_main_road[0]
            sytuation_on_main_road = sytuation_on_main_road[1:]
            whoose_turn = 'side street'
            break
        if whoose_turn == 'side street':
            for side_street_car in sytuation_on_side_streets:
                if len(side_street_car) > 0 and side_street_car[0] != final_line[-1]: 
                    side_street_car = side_street_car[1:]
                    whoose_turn = 'main road'
                    pointer = side_street_car[0]
                    break
    
    return final_line


print(traffic_jam("abcX", ["","","BBBBBB","","","","","CCCCC"]))
                    

