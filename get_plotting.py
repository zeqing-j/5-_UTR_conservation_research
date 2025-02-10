import pandas as pd
import plotly.express as px

# Replace 'your_file.xlsx' with the path to your Excel file
file_path = r'C:\Users\JZQ\Downloads\updated_alifold_excel.xlsx'
column1 = 'MFE from Linearalifold'
column2 = 'CAI_values'
gene_name = 'geneSymbol'  # The name of the column with gene (transcript) IDs

# Read the Excel file
df = pd.read_excel(file_path)

# Clean the data: remove rows where either column has undefined values
df_cleaned = df.dropna(subset=[column1, column2, gene_name])

# Create an interactive scatter plot
fig = px.scatter(df_cleaned, x=column1, y=column2, hover_data=[gene_name],
                 labels={
                     column1: 'MFE from Linearalifold (kJ/mol)',
                     column2: 'CAI_values',
                     gene_name: 'geneSymbol'
                 })

# Show the figure
fig.show()
fig.write_html('CAI_linMFE.html', auto_open=True)