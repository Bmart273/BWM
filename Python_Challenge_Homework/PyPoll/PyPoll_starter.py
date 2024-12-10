# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data, delimiter= ",")

# Skip the header row
    csv_header = next(reader)

# Initialize variables to track the election data
# Winning Candidate and Winning Count Tracker
    total_votes = 0
    vote_count = 0
    winning_vote_count = 0
    winning_candidate = ""

# Define lists and dictionaries to track candidate names and vote counts
    candidate_list =[]
    subsidized_cand_list =[]
    candidate_cnt_list =[]
    candidate_pct_list =[]


# Loop through each row of the dataset and process it

    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ",end="")
        candidate_list.append(row[2])

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate = row[2]
        if candidate not in subsidized_cand_list:
            subsidized_cand_list.append(candidate)
    
    for candidate_name in subsidized_cand_list:

        for value in candidate_list:

            # Calculate total and percentage votes for each Unique Candidate name
            if value == candidate_name:
                vote_count += 1
    # Print the total vote count (to terminal)
        print(f'"Total Votes: {total_votes}')

 # Loop through the candidates to determine vote percentages and identify the winner
        candidate_vote_percentage = round(((vote_count/total_votes)*100),3)

        candidate_cnt_list.append(vote_count)
        candidate_pct_list.append(candidate_vote_percentage)

        if vote_count > winning_vote_count:
            winning_vote_count = vote_count
            winning_candidate = candidate_name

        vote_count = 0


# Generate and print the winning candidate summary

print(f'Election Results')
print('----------------------------')
print(f'Total Votes: {total_votes}')
print('----------------------------')
for (name, percentage, count) in zip(subsidized_cand_list, candidate_pct_list, candidate_cnt_list):
    print(f"{name}: {percentage}% ({count})")
print(f'----------------------------') 
print(f'Winner: {winning_candidate}')
print(f'----------------------------')


    # Save the winning candidate summary to the text file
with open(file_to_output, "w") as datafile:
    datafile.write(f'Election Results\n')
    datafile.write(f'----------------------------\n')
    datafile.write(f'Total Votes: {total_votes}\n')
    datafile.write(f'----------------------------\n')
    for (name, percentage, count) in zip(subsidized_cand_list, candidate_pct_list, candidate_cnt_list):
        datafile.write(f'{name}: {percentage}% ({count})\n')
    datafile.write(f'----------------------------\n')
    datafile.write(f'Winner: {winning_candidate}\n')
    datafile.write(f'----------------------------\n')
