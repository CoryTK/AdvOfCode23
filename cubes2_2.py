#https://adventofcode.com/2023/day/2
# Going for 2x Gold Stars

import re

input_as_list = []                              #placeholder list for the input data
with open("cubes2.csv") as file:      #import actual data into the placeholder list
    for line in file:
        input_as_list.append(line.rstrip())

# separate game number and rounds by the ":" and create a list of rounds as ints
game_number = []
rounds = []
for row in input_as_list:
    game_raw, rounds_raw = row.split(": ")      #separates by the comma
    digits = re.search(r"Game ([0-9]{1,3})", game_raw)
    game_number.append(int(digits[1]))   #sets the list of rounds as ints
    rounds.append(rounds_raw)               #creates a list rounds made up of strings of the data right of the ": "

clean_rounds = []
for roll in rounds:                 # for each row in rounds
    #split the round strings into their own lists of items separated by a " "
    outcomes = roll.split(" ")
    clean_outcomes = []

    # clean each word in outcomes
    for g in outcomes:              
        clean_outcomes.append(g.replace(",","").replace(";",""))

    clean_rounds.append(clean_outcomes) # creates a clean list of each round to iterate over


#putting function above it's use use cause i didn't create a main() and so spaghetti code **BAM!**
def get_cubed_value(row):            
    red = int(0)
    green = int(0)
    blue = int(0)
    for i in range(len(row)):     
        if row[i].isdigit():
            if row[i + 1] == "red":
                if int(row[i]) > red:
                    red = int(row[i])
            elif row[i + 1] == "green":   
                if int(row[i]) > green:
                    green = int(row[i])                
            elif row[i + 1] == "blue":
                if int(row[i]) > blue:
                    blue = int(row[i])                
            else:
                pass
    print(red, green, blue)    
    print( red * green * blue)
    return red * green * blue

score = int(0)
for each_row in range(len(clean_rounds)):
    score += get_cubed_value(clean_rounds[each_row])

print(score)
