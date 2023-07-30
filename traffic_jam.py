def traffic_jam(main_road, side_streets):
   final_line = []
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

   while len(final_line) != total_cars:
      count = 0
      if len(main_road) > 0:
         final_line.append(main_road[0])
         main_road = main_road[1:]
         if count != 1:
            for i in range(how_many_side_streets_occupied):   
               if side_str_num_and_cars_on_it[i][1] > 0:   
                  if main_road[side_str_num_and_cars_on_it[i][0]-1] != side_str_num_and_cars_on_it[i][2]:
                     main_road = main_road[:side_str_num_and_cars_on_it[i][0]] + str(side_str_num_and_cars_on_it[i][2]) + main_road[side_str_num_and_cars_on_it[i][0]:]
                     side_str_num_and_cars_on_it[i][1] -= 1
                     count += 1
      
   final_line = ''.join(final_line)
   final_line = final_line[:final_line.find('X')+1]   

   return final_line




print(traffic_jam("abcdefX", []), "abcdefX")
print(traffic_jam("abcXdef", []), "abcX")
print(traffic_jam("Xabcdef", []), "X")
print(traffic_jam("abcdefghijklmX", ["","","","BBBBBB","","","","","CCCCC"]))
print(traffic_jam("abcdeXghi", ["","","CCCCC","","EEEEEEEEEE","FFFFFF","","","IIIIII"]))


#traffic_jam("abcdefghijklmX", ["","","","BBBBBB","","","","","CCCCC"]), "abcdBeBfBgBhBiBCjCkClCmCX")
#test.assert_equals(traffic_jam("abcdeXghi", ["","","CCCCC","","EEEEEEEEEE","FFFFFF","","","IIIIII"]), "abcCdCeCECX")

#'abcCdCECFCECFEFEFEEFEIEIEEFIIeX' should equal 'abcCdCeCECX'
#'abcdBeBfBgBhBCBiCCjCCklmX' should equal 'abcdBeBfBgBhBiBCjCkClCmCX'  
# --> traffic_jam("abcdefghijklmX", ["","","","BBBBBB","","","","","CCCCC"]), "abcdBeBfBgBhBiBCjCkClCmCX")
   