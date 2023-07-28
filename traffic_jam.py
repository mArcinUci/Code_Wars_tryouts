def traffic_jam(main_road, side_streets):
   the_line = []
   side_str_num_and_cars_on_it = []

   count_side_streets_cars = 0

   how_many_side_streets = len(side_streets)
   len_main_road = len(main_road)
   
   for i in range(how_many_side_streets):
      
      if len(side_streets[i])>0:
         side_str_num_and_cars_on_it.append([i,int(len(side_streets[i])),side_streets[i][0]])
         count_side_streets_cars += len(side_streets[i])
         
   total_cars = len_main_road + count_side_streets_cars
   how_many_side_streets_occupied = len(side_str_num_and_cars_on_it)

   while len(the_line) != total_cars:
      if len(main_road) > 0:
         the_line.append(main_road[0])
         main_road = main_road[1:]

         for i in range(how_many_side_streets_occupied):
            if side_str_num_and_cars_on_it[i][1] > 0:
               if main_road[side_str_num_and_cars_on_it[i][0]-1] != side_str_num_and_cars_on_it[i][2]:
                  main_road = main_road[:side_str_num_and_cars_on_it[i][0]] + str(side_str_num_and_cars_on_it[i][2]) + main_road[side_str_num_and_cars_on_it[i][0]:]
                  side_str_num_and_cars_on_it[i][1] -= 1
         
   the_line = ''.join(the_line)

   
   print(side_str_num_and_cars_on_it)
   print(the_line)
 

traffic_jam("abcdefghijklmX", ["","","","BBBBBB","","","","","CCCCC"])



#traffic_jam("abcdefghijklmX", ["","","","BBBBBB","","","","","CCCCC"]), "abcdBeBfBgBhBiBCjCkClCmCX")