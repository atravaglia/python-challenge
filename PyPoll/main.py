# Importing os and csv file 
import os
import csv

# Create path to CSV file
election_data_csv = os.path.join("Resources","election_data.csv")

#variables
total_votes = []
candidates_unique = []
candidate_vote_count = []

# Create paths
with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    # Read each row of data after header
    for row in csvreader:
        # total votes
        total_votes.append(row[0])
        #candidates
        candidate_in = (row[2])
        #if candidate alreaady included in the list: associate index to candidate and add 1 to vote count
        if candidate_in in candidates_unique:
            candidate_index = candidates_unique.index(candidate_in)
            candidate_vote_count[candidate_index] = candidate_vote_count[candidate_index] + 1
        else:
            #if candidate  not included in the list: include in the list and add 1 to vote count
            candidates_unique.append(candidate_in)
            candidate_vote_count.append(1)

percent = []
max_votes = candidate_vote_count[0]
max_index = 0
total_votes_length = len(total_votes)

for x in range(len(candidates_unique)):
    # calculate %
    vote_percent = round(candidate_vote_count[x]/total_votes_length*100, 2)
    percent.append(vote_percent)
    
    if candidate_vote_count[x] > max_votes:
        max_votes = candidate_vote_count[x]
        max_index = x

election_winner = candidates_unique[max_index] 

# Print results 

print('Election Results')

print("..................")

print(f'Total Votes: {total_votes_length}')

print("..................")

for x in range(len(candidates_unique)):
    print(f'{candidates_unique[x]} : {percent[x]}% ({candidate_vote_count[x]})')

print(f'Election Winner: {election_winner}')

# Write output

with open("Analysis/output.txt", "w") as txtfile:
   
    txtfile.write("Election Results" + "\n")

    txtfile.write(".............................. \n")

    txtfile.write(f'Total Votes: {total_votes_length}\n')

    txtfile.write("............................... \n")

    for x in range(len(candidates_unique)):
        txtfile.write(f'{candidates_unique[x]} : {percent[x]}% ({candidate_vote_count[x]})\n')
    
    txtfile.write(f'Election Winner: {election_winner}\n')
   
    txtfile.close()
