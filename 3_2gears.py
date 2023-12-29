# https://adventofcode.com/2023/day/3
# A gear is any * symbol that is adjacent to exactly two part numbers
# gear ratio is the result of multiplying those two numbers together

input_as_list = []                              #placeholder list for the input data
#with open("3_2gears_test_data.csv") as file:      #import actual data into the placeholder list
with open("3gears_input_data.csv") as file:
    for line in file:
        new_line = '.'+ line.rstrip() + '.'
        input_as_list.append(new_line)



#function for checking a row of numbers starting with a root number
def horizontal_check(five_letters):
    variable = ''
    if five_letters[2].isdigit():               #starting digit
        variable = variable + five_letters[2] 
        if five_letters[3].isdigit():               #one right
            variable = variable + five_letters[3]
            if five_letters[4].isdigit():             #two right
                variable = variable + five_letters[4]
        if five_letters[1].isdigit():               #one left 
            variable = five_letters[1] + variable
            if five_letters[0].isdigit():             #two left
                variable = five_letters[0] + variable
    return variable         

#find all the *'s
score = int(0)

for row_num in range(len(input_as_list)):
    for col_num in range(len(input_as_list[row_num])):
        if input_as_list[row_num][col_num] == "*":
            print(f"Row: {row_num}, Col: {col_num}")
        
            #check for values and check if there are 2 numbers attached to each
            two_values = []
            temp_var =''

            #check values to the left of "*"
            if input_as_list[row_num][col_num-1].isdigit():
                temp_var = input_as_list[row_num][col_num-1] + temp_var
                if input_as_list[row_num][col_num-2].isdigit():
                    temp_var = input_as_list[row_num][col_num-2] + temp_var
                    if input_as_list[row_num][col_num-3].isdigit():
                        temp_var = input_as_list[row_num][col_num-3] + temp_var
                if temp_var != '':
                    two_values.append(temp_var)    
                    temp_var = '' 

            #check values to the right of "*"
            if input_as_list[row_num][col_num+1].isdigit():
                temp_var = temp_var + input_as_list[row_num][col_num+1] 
                if input_as_list[row_num][col_num+2].isdigit():
                    temp_var = temp_var + input_as_list[row_num][col_num+2]
                    if input_as_list[row_num][col_num+3].isdigit():
                        temp_var = temp_var + input_as_list[row_num][col_num+3]
                if temp_var != '':
                    two_values.append(temp_var)    
                    temp_var = ''        
                       
            temp_var = horizontal_check(input_as_list[row_num-1][col_num-3:col_num+2])
            if temp_var != '':
                two_values.append(temp_var)
                temp_var = ''


            #check values in position top-middle (-1, 0)
            if input_as_list[row_num-1][col_num-1].isdigit():
                pass
            else:
                temp_var = horizontal_check(input_as_list[row_num-1][col_num-2:col_num+3])
                if temp_var != '':
                    two_values.append(temp_var)
                    temp_var = ''

            #check values in position top-right (-1, +1)
            if input_as_list[row_num-1][col_num].isdigit():            
                pass
            else:
                temp_var = horizontal_check(input_as_list[row_num-1][col_num-1:col_num+4])
                if temp_var != '':
                    two_values.append(temp_var)
                    temp_var = ''

            #check values in position bottom left
            temp_var = horizontal_check(input_as_list[row_num+1][col_num-3:col_num+2])
            if temp_var != '':
                two_values.append(temp_var)
                temp_var = ''

            #check values in position bottom middle
            if input_as_list[row_num+1][col_num-1].isdigit(): 
                pass
            else:
                temp_var = horizontal_check(input_as_list[row_num+1][col_num-2:col_num+3])
                if temp_var != '':
                    two_values.append(temp_var)
                    temp_var = ''                
            
            # check values in position bottom right
            if input_as_list[row_num+1][col_num].isdigit(): 
                pass
            else:            
                temp_var = horizontal_check(input_as_list[row_num+1][col_num-1:col_num+4])
                if temp_var != '':
                    two_values.append(temp_var)
                    temp_var = ''    

            print(two_values)
            if len(two_values) ==2:
                score += int(two_values[0]) * int(two_values[1])

print(score)



# find every "*" recording its position
    #check the 2D array around it for numbers
        #if there is a number, check the adjacent spots to grab the full number
            #consider collecting in pairs for tracability
