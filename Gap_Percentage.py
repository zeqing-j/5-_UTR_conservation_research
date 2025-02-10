import os
import sys

def gap_percentage(filename):
    # print the percentage of dashes in each column for all species
    with open(filename, 'r') as file:
        lines = file.readlines() 
    # store counts of "-" in each column as a list
    dash_count = [0] * len(lines[1].strip())

    # Iterate through each line skipping lines starting with "<"
    num_species = 0
    for line in lines:
        if line.startswith(">"):
            continue
        else:
            # count the total number of base in each column
            num_species += 1
            for i, char in enumerate(line.strip()):
                if char == "-":
                    dash_count[i] += 1

    # Calculate the percentage of dashes in each column
    dash_percentages = [(count / num_species) * 100 for count in dash_count]

    return dash_percentages

# Test the function with your file name
percentages = gap_percentage(r"C:\Users\JZQ\Downloads\CDKN1B.fasta")
print(percentages)