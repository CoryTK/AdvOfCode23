#https://adventofcode.com/2023/day/2
# trying with Lists

#practice_list = [
#    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
#    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
#    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
#    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
#    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
#]
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

#print(game_number)
#print(rounds)

clean_rounds = []
for roll in rounds:                 # for each row in rounds
    #split the round strings into their own lists of items separated by a " "
    outcomes = roll.split(" ")
    clean_outcomes = []

    # clean each word in outcomes
    for g in outcomes:              
        clean_outcomes.append(g.replace(",","").replace(";",""))

    clean_rounds.append(clean_outcomes) # creates a clean list of each round to iterate over

#print(clean_rounds)

#putting function above it's use use cause i didn't create a main() and so spaghetti code **BAM!**
def check_if_possible(row):            # check if all values in each row < max values, if so, return false
    counter = 0
    for i in range(len(row)):     
        if row[i].isdigit():
            if row[i + 1] == "red" and int(row[i]) > 12:
                counter += 1
            elif row[i + 1] == "green" and int(row[i]) > 13:   
                counter += 1
            elif row[i + 1] == "blue" and int(row[i]) > 14:
                counter +=1
            else:
                pass
    if counter == 0:
        return True    

score = int(0)
for each_row in range(len(clean_rounds)):
    #print(clean_rounds[row])
    #print(game_number[row])
    #print("----")
    if check_if_possible(clean_rounds[each_row]):
        #print(game_number[each_row], "Passed")
        score += game_number[each_row]
    else:
        pass
        #print(game_number[each_row], "Check ", clean_rounds[each_row])


print(score)






