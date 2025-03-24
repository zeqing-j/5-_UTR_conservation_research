import os
import sys

def gap_percentage(filename):
    with open(filename, 'r') as file:
        lines = file.readlines() 
    dash_count = [0] * len(lines[1].strip())
    num_species = 0
    for line in lines:
        if line.startswith(">"):
            continue
        else:
            num_species += 1
            for i, char in enumerate(line.strip()):
                if char == "-":
                    dash_count[i] += 1

    dash_percentages = [(count / num_species) * 100 for count in dash_count]

    return dash_percentages

percentages = gap_percentage(r"C:\Users\JZQ\Downloads\CDKN1B.fasta")
print(percentages)
