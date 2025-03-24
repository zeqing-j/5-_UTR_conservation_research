import matplotlib.pyplot as plt

input_file = r'C:\Users\JZQ\Downloads\bp_percentage.txt'  
output_file = r'C:\Users\JZQ\Downloads\histogram.png'  

percentages = []

with open(input_file, 'r') as file:
    lines = file.readlines()
    for line in lines:
        parts = line.strip().split(':') 
        if len(parts) == 2:
            percentage_str = parts[1].replace('%', '') 
            try:
                percentage = float(percentage_str)
                percentages.append(percentage)
            except ValueError:
                continue

# Create a histogram with 10 bins
plt.figure(figsize=(10, 6))  
values, bins, bars = plt.hist(percentages, bins=10, color='blue', alpha=0.7, edgecolor='black')
plt.xlabel('Percentage')
plt.ylabel('Frequency')
plt.title('Distribution of Gene bp Percentages')
plt.bar_label(bars, fontsize=20, color='navy')
plt.savefig(output_file)
