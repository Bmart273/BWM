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
previous_profits = ""
change = 0
total_changes = 0
change_times = 0
date_list = []
profit_loss_list = []
changes_list =[]
greatest_overall_increase = {"date":"", "amount":0}
greatest_overall_decrease = {"date":"", "amount":0}
# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:

        date_list.append(row[0])
        profit_loss_list.append(row[1])
        
        # Track the total
        total_net += int(row[1])
        # Track the net change
        profit_loss = int(row[1])

        if previous_profits != "":
            change  = profit_loss - previous_profits
            changes_list.append(change)

            total_changes += int(change)
        previous_profits= profit_loss

        # Calculate the greatest increase in profits (month and amount)
        if change > greatest_overall_increase["amount"]:
            greatest_overall_increase["amount"] = change
            greatest_overall_increase["date"] = row[0]

        # Calculate the greatest decrease in losses (month and amount)
        if change < greatest_overall_decrease["amount"]:
            greatest_overall_decrease["amount"] = change
            greatest_overall_decrease["date"] = row[0] 


# Calculate the average net change across the months
total_months = len(date_list)

change_times = len(changes_list)
average_change = round((total_changes / change_times), 2)

# Generate the output summary and print the output

print(f'Financial Analysis')
print(f'----------------------------')
print(f'Total Months = {total_months}')
print(f'Total: ${total_net}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {greatest_overall_increase["date"]} (${greatest_overall_increase["amount"]})')
print(f'Greatest Decrease in Profits: {greatest_overall_decrease["date"]} (${greatest_overall_decrease["amount"]})')

# Write the results to a text file
with open(file_to_output, "w") as PyBanktxt_file:
    PyBanktxt_file.write(f'Financial Analysis\n')
    PyBanktxt_file.write(f'----------------------------\n')
    PyBanktxt_file.write(f'Total Months = {total_months}\n')
    PyBanktxt_file.write(f'Total: ${total_net}\n')
    PyBanktxt_file.write(f'Average Change: ${average_change}\n')
    PyBanktxt_file.write(f'Greatest Increase in Profits: {greatest_overall_increase["date"]} (${greatest_overall_increase["amount"]})\n')
    PyBanktxt_file.write(f'Greatest Decrease in Profits: {greatest_overall_decrease["date"]} (${greatest_overall_decrease["amount"]})')