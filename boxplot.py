import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\JZQ\Downloads\cai.xlsx"  
df = pd.read_excel(file_path)

low_energy_df = df[df['Minimum Free Energy (80nts)'] < -25]
high_energy_df = df[df['Minimum Free Energy (80nts)'] > -25]
low_energy_df['Category'] = 'Low Energy'
high_energy_df['Category'] = 'High Energy'
combined_df = pd.concat([high_energy_df, low_energy_df])

# Create a boxplot based on proline count for the two categories
plt.figure(figsize=(10, 6))
sns.boxplot(x='Category', y='CAI_count', data=combined_df)
medians = combined_df.groupby(['Category'])['CAI_count'].median()
for category in medians.index:
    plt.text(medians.index.get_loc(category), medians[category], f'{medians[category]:.2f}',
             horizontalalignment='center', size='medium', color='w')
plt.title('CAI Boxplot for Transcripts with Different Energy Levels')
plt.xlabel('Energy Category')
plt.ylabel('high CAI count')
plt.show()
