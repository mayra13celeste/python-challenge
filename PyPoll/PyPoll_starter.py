# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
winning_vote_count = 0

# Define lists and dictionaries to track candidate names and vote counts
candidates = []
vote_count = []
total_candidates = []
election_dict = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = []

# Open the CSV file and process it
with open(file_to_load, mode='r') as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # track total votes and candidates
    total_votes = 0
    total_candidates = []
    candidates = []
    ballot = []

    # Loop through each row of the dataset and process it
    for row in reader:
        ballot.append(row[0])

        # calculate total votes
        total_votes = len(ballot)

        # Get the candidate's name from the row
        total_candidates.append(row[2])
                             
        # If the candidate is not already in the candidate list, add them
        if row[2] not in candidates:
            candidates.append(row[2])
            
    # Add a vote to the candidate's count
    for candidate in candidates:
        vote_count.append(total_candidates.count(candidate))
        
# making dictionary with candidates as keys and vote count as values
election_dict = dict(zip(candidates, vote_count))

# assign election winner as max value of election_dict
winning_candidate = max(election_dict, key=election_dict.get)

   
# create output variables
output_line_1 = "Election Results"
output_line_2 = "---------------------------------"
output_line_3 = "Total Votes: " + str(total_votes)
output_line_4 = "---------------------------------"
output_line_6 = "---------------------------------"
output_line_7 = "Winner: " + str(winning_candidate)
output_line_8 = "---------------------------------"

# print the output
print(output_line_1)
print(output_line_2)
print(output_line_3)
print(output_line_4)

# calculating percentage of votes each candidate won and putting together the election dictionary
for x in election_dict:
    output_line_5 = (f"{x}: {format(float(election_dict[x] / total_votes) , ' .3%')} ({election_dict[x]})")
    print(output_line_5)
    
print(output_line_6)
print(output_line_7)
print(output_line_8)
            
# write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output_line_1 + "\n")
    txt_file.write(output_line_2 + "\n")
    txt_file.write(output_line_3 + "\n")
    txt_file.write(output_line_4 + "\n")
    for x in election_dict:
        output_line_5 = (f"{x}: {format(float(election_dict[x] / total_votes) , ' .3%')} ({election_dict[x]})")
        txt_file.write(output_line_5 + "\n")
    txt_file.write(output_line_6 + "\n")
    txt_file.write(output_line_7 + "\n")
    txt_file.write(output_line_8 + "\n")