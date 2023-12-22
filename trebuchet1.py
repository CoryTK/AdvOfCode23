
#practice_list = [              #test data 
#    "1abc2",
#    "pqr3stu8vwx",
#    "a1b2c3d4e5f",
#    "treb7uchet",
#]
input_as_list = []                              #placeholder list for the input data
with open("trebuchet1_input.csv") as file:      #import actual data into the placeholder list
    for line in file:
        input_as_list.append(line.rstrip())

final_list = []

#get list of numbers
for i in input_as_list:         # loop over each row
    loop_list = []              # list for each word in practice_list that will wipe after each word
    for c in i:                 # loop over each character
        if c.isdecimal():           # check if a number
            loop_list.append(c)     # append the number to the temporary list
    final_list.append(loop_list)    # at the end of each word, append the loop list to the final list

# for loop with list of numbers, print the first number and the last number into a string of numbers
total_sum = 0
for i in final_list:
    number = int(i[0] + i[-1])
    total_sum += number

print (total_sum)

#answer = 56506


