# https://adventofcode.com/2023/day/3
# IF there is a symbol adjacent to a number above, below, or next, then print the number

#iterable list of rows

input_as_list = []                              #placeholder list for the input data
#with open("3gears_test_data.csv") as file:      #import actual data into the placeholder list
with open("3gears_input_data.csv") as file:
    for line in file:
        new_line = '.'+ line.rstrip() + '.'
        input_as_list.append(new_line)

#print(input_as_list)

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "+", "-", "=","/"]

#find numbers and check values
final_parts = []
for row_num in range(0, len(input_as_list)-1):
    for col_num in range(0, len(input_as_list[row_num])-1):
        temp_var = []

        if col_num >0 and input_as_list[row_num][col_num-1].isdigit():
            pass
        
        elif input_as_list[row_num][col_num].isdigit():
            temp_var.append(input_as_list[row_num][col_num])
            if input_as_list[row_num][col_num+1].isdigit():
                temp_var.append(input_as_list[row_num][col_num+1])
                if input_as_list[row_num][col_num+2].isdigit():
                    temp_var.append(input_as_list[row_num][col_num+2])
            
            
            start_row, end_row = row_num -1, row_num + 1 
            start_col, end_col = col_num - 1, col_num + len(temp_var)

            for rowz in range(start_row,end_row + 1):
                for colz in range(start_col, end_col + 1):
                    if input_as_list[rowz][colz] in symbols:
                        #print(f"row: {rowz}, col {colz}")
                        #print(''.join(temp_var))
                        final_parts.append(''.join(temp_var))

print(final_parts)

total = int(0)
for x in final_parts:
    total += int(x)

print(total)  # this code currently omits the last row - add manually to get the right answer!


#first attempt answer = 513292  LOW
#second attempt answer = 534211 (added "=" to symbols) LOW
#third attempt answer = 535728 (removed starting buffer)
#4th attempt answer = 539433 (manually added last row with calculator cause need buffer to work but it ignores last row)


#Parse out the numbers identifying the position
    #Option 1, 
        #grab every number and put into a single list (num_list)
        #iterate each line until a number is hit, check the length of the num_list currently incremented, if the character to the left is a digit, skip
        # check all adjacent spots according to the position of the digit
            #line above, character -1, through the length of the word, to character + length
            #same line, character -1 and character + length
            #line below, character -1, though the length of the word, to character + length

#Get list of numbers to be referenced
#num_list = []
#for line in input_as_list:      #get all the non"." and non"" characters
#    numbers = line.split(".")
#    for x in numbers:
#        if x != "":
#            num_list.append(x)
#        else:
#            pass
#print(num_list)

# remove the symbols to create a clean number list
#final_num_list = []
#for y in num_list:
#    new_num = y.strip("!").strip("@").strip("#").strip("$").strip("%").strip("^").strip("&").strip("*").strip("+").strip("-").strip("/").strip("=")
#    if new_num != "":
#        final_num_list.append(new_num)
#print(final_num_list)


##REDDIT SUDO CODE
    #1. First for conveniency, I did preprocessing to add a guardband area in all four directions (add extra "." on each four borders) of the 2D map so that my code would not later need to handle accessing out of bounds of the map.

    #2. I loaded the map into a 2D array so I could easily do map[y][x] indexing on it to find the character in each map coordinate.

    #3. Then I scanned through the map top-down, left-to-right, skipping the guardband I created, i.e. in
            #for y in 1...height-2:
                #for x in 1...width-2:
        #order (0-indexing, since the guardband would be at x/y=0 and x=width-1 and y=height-1)

    #4. While scanning, whenever I would find a digit at [y][x], e.g. a "3", I'd then scan forward to find how many characters wide that number would be, e.g. "345" -> three characters.

    #5. Based on that info, for example, "(x,y) is the start position of a number that is three digits long", I would calculate bounding box map coordinates around the newly found number that is one coordinate bigger than the number in each direction. This bounding box will have extremes x0->x1 and y0->y1.

    #6. Then I would have a helper function does_symbol_exist_inside_rectangle(x0,x1,y0,y1), that loops over the given rectangular area on the map, and returns true if a symbol is found inside it.

    #7. Accumulate to the result. Then skip forward past all digits of the current number (since all its chars are now processed), and go back to continue looping at step 3.
        