
#import modules to read csv file
import os
import csv

#define path for the csv file
csvpath = os.path.join('Resources', 'election_data.csv')

#declarations
row_count = 0
candidate_votes = {}

#open the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip the header row, since it shouldn't be included in the calculations
    next(csvreader)

    #iterating through each row  
    for row in csvreader:

        #count the total # of votes (1 vote per row)
        row_count += 1
        
        #get candidate name from row, located in column 3
        candidate = row[2]

        #check if name is in the candidate_votes dictionary and if yes, increment vote count by 1
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1

            #if not in dictionary, add to it and start the count at 1
        else:
            candidate_votes[candidate] = 1

#print beginning of analysis and total votes
print("Election Results")
print("----------------------------")
print(f"Total Votes: {row_count}")
print("----------------------------")

#calculate the percentage of total votes each candidate received
for candidate, votes in candidate_votes.items():
    percentage = ((votes/row_count) * 100)

    #loop through to print the results for each candidate
    print(f"{candidate}: {percentage:.3f}% ({votes})")

#determine the winner
#the .get function retrieves the value associated with the candidate from the dictionary
winner = max(candidate_votes, key=candidate_votes.get)

#print the winner's name and make it fancy
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

#write analysis to text file
txtfile_Path = os.path.join('Analysis', 'results.txt')
with open(txtfile_Path, "w") as txtfile:

    txtfile.write("Election Results\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Votes: {row_count}\n")
    txtfile.write("----------------------------\n")

    #have to calculate the percentages again, since it's in a for loop
    for candidate, votes in candidate_votes.items():
        percentage = ((votes/row_count) * 100)
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("----------------------------\n")
