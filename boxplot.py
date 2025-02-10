import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
file_path = r"C:\Users\JZQ\Downloads\cai.xlsx"  # Replace with your file path
df = pd.read_excel(file_path)

# Separate transcripts based on minimum free energy
low_energy_df = df[df['Minimum Free Energy (80nts)'] < -25]
high_energy_df = df[df['Minimum Free Energy (80nts)'] > -25]

# Combine the two categories for plotting
low_energy_df['Category'] = 'Low Energy'
high_energy_df['Category'] = 'High Energy'
combined_df = pd.concat([high_energy_df, low_energy_df])

# Create a boxplot based on proline count for the two categories
plt.figure(figsize=(10, 6))
sns.boxplot(x='Category', y='CAI_count', data=combined_df)

# Add median labels
medians = combined_df.groupby(['Category'])['CAI_count'].median()
for category in medians.index:
    plt.text(medians.index.get_loc(category), medians[category], f'{medians[category]:.2f}',
             horizontalalignment='center', size='medium', color='w')

# Set plot title and labels
plt.title('CAI Boxplot for Transcripts with Different Energy Levels')
plt.xlabel('Energy Category')
plt.ylabel('high CAI count')

# Show the plot
plt.show()
