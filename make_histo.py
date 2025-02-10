# Step 3: Python script to read the text file, create a histogram, and save it to an output file
import matplotlib.pyplot as plt

# Read the text file
input_file = r'C:\Users\JZQ\Downloads\bp_percentage.txt'  # Replace with your input text file name
output_file = r'C:\Users\JZQ\Downloads\histogram.png'  # Output file for the histogram

# Initialize a list to store the percentages
percentages = []

# Open the input file and read the lines
with open(input_file, 'r') as file:
    lines = file.readlines()
    # Extract the percentage value from each line
    for line in lines:
        # Assuming the line format is 'gene_name:percentage%'
        # Example line: 'gene_ABC:45%'
        parts = line.strip().split(':')  # Split by the colon
        if len(parts) == 2:
            # Remove the '%' and convert to a float
            percentage_str = parts[1].replace('%', '')  # Extract the percentage part
            try:
                percentage = float(percentage_str)
                percentages.append(percentage)
            except ValueError:
                # If there's an error converting to float, continue to the next line
                continue

# Create a histogram with 10 bins
plt.figure(figsize=(10, 6))  # Optional: Set the size of the plot
values, bins, bars = plt.hist(percentages, bins=10, color='blue', alpha=0.7, edgecolor='black')

# Set the labels and title
plt.xlabel('Percentage')
plt.ylabel('Frequency')
plt.title('Distribution of Gene bp Percentages')
plt.bar_label(bars, fontsize=20, color='navy')

# Save the histogram to the output file
plt.savefig(output_file)

print(f"Histogram saved to {output_file}")
