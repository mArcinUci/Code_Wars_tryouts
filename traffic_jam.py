def traffic_jam(main_road, side_streets):
   active_str_num_and_cars_on_it = []

   count_side_streets_cars = 0

   how_many_side_streets = len(side_streets)
   len_main_road = len(main_road)
   
   for i in range(how_many_side_streets):
      
      if len(side_streets[i])>0:
         
         active_str_num_and_cars_on_it.append([i,len(side_streets[i])])
         count_side_streets_cars += len(side_streets[i])
         print('--->' + str(count_side_streets_cars))
         
   total_cars = len_main_road + count_side_streets_cars
   how_many_side_streets_occupied = len(active_str_num_and_cars_on_it)

   
   


   print(how_many_side_streets_occupied)
   print(active_str_num_and_cars_on_it)
   print(total_cars)


traffic_jam("abcdefghijklmX", ["","","","BBBBBB","","","","","CCCCC"])



#traffic_jam("abcdefghijklmX", ["","","","BBBBBB","","","","","CCCCC"]), "abcdBeBfBgBhBiBCjCkClCmCX")