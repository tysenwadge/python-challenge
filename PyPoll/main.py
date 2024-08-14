#Importing the necessary libraries
import os
import csv

election_data = os.path.join("Resources","election_data.csv")

# Setting list to store names of candidates
candidates_name = []

# Setting list to store number of votes
vote_number = []

# Setting list to store percentage of total votes
vote_percent = []

# A counter for number of votes 
vote_total = 0

#reading and determining header row from class examples
with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        # Add to our counter
        vote_total += 1 

        #If statement to add our candidate names to the list, if name isn't in list - add to list.
        #If name appears and is already in list, add to vote count

        if row[2] not in candidates_name:
            candidates_name.append(row[2])
            index = candidates_name.index(row[2])
            vote_number.append(1)
        else:
            index = candidates_name.index(row[2])
            vote_number[index] += 1
    
    # Calculating vote percentage and adding to list
    for votes in vote_number:
        percentage = (votes/vote_total) * 100
        percentage = "%.3f%%" % percentage
        vote_percent.append(percentage)
    
    # Get the winner
    winner = max(vote_number)
    index = vote_number.index(winner)
    winning_candidate = candidates_name[index]

# Displaying results and formatting output
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(vote_total)}")
print("--------------------------")
for i in range(len(candidates_name)):
    print(f"{candidates_name[i]}: {str(vote_percent[i])} ({str(vote_number[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

# Exporting to .txt file in Analysis folder/String format research outside example
output = open("Analysis/output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(vote_total)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates_name)):
    line = str(f"{candidates_name[i]}: {str(vote_percent[i])} ({str(vote_number[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))