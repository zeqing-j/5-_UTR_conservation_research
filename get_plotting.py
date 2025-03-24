import pandas as pd
import plotly.express as px


file_path = r'C:\Users\JZQ\Downloads\updated_alifold_excel.xlsx'
column1 = 'MFE from Linearalifold'
column2 = 'CAI_values'
gene_name = 'geneSymbol'  

df = pd.read_excel(file_path)

df_cleaned = df.dropna(subset=[column1, column2, gene_name])

fig = px.scatter(df_cleaned, x=column1, y=column2, hover_data=[gene_name],
                 labels={
                     column1: 'MFE from Linearalifold (kJ/mol)',
                     column2: 'CAI_values',
                     gene_name: 'geneSymbol'
                 })

fig.show()
fig.write_html('CAI_linMFE.html', auto_open=True)
