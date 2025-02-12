# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os


# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path


# Define variables to track the financial data
total_months = 0
total_net = 0


# Open and read the csv
with open(file_to_load, mode='r') as financial_data:
    reader = csv.reader(financial_data)

    #grab the first row from file that represents header
    header = next(reader)
   
    # Track the total and net change
    total_net = []
    date = []

    # Process each row of data
    for row in reader:
        # Track the total
        total_net.append(int(row[1]))
        date.append(row[0])

    # Track the net change
    changes = []
    for i in range(1, len(total_net)):
        change = total_net[i] - total_net[i - 1]
        changes.append(change)


    # calculate the total months
    total_months = len(date) 

    # Calculate the greatest increase in profits (month and amount)
    greatest_increase = max(changes)

    # Calculate the greatest decrease in losses (month and amount)
    greatest_decrease = min(changes)

    # Calculate the average net change across the months
    net_average =round(sum(changes) / len(changes), 2) 

# Create output variables
output_line_1 = "Financial Analysis"
output_line_2 = "----------------------------"
output_line_3 = "Total Months: " + str(total_months)
output_line_4 = "Total: " + "$ " + str(sum(total_net))
output_line_5 = "Average Change: " + "$ " + str(net_average)
output_line_6 = "Greatest Increase in Profits: " + str(date[changes.index(max(changes))+1]) + " ($" + str(greatest_increase) + ")"
output_line_7 = "Greatest Decrease in Profits: " + str(date[changes.index(min(changes))+1]) + " ($" + str(greatest_decrease) + ")"

# Print the output
print(output_line_1)
print(output_line_2)
print(output_line_3)
print(output_line_4)
print(output_line_5)
print(output_line_6)
print(output_line_7)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output_line_1 + "\n")
    txt_file.write(output_line_2 + "\n")
    txt_file.write(output_line_3 + "\n")
    txt_file.write(output_line_4 + "\n")
    txt_file.write(output_line_5 + "\n")
    txt_file.write(output_line_6 + "\n")
    txt_file.write(output_line_7 + "\n")
    txt_file.close()