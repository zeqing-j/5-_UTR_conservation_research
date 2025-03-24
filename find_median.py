import pandas as pd

def process_excel(input_file, output_file):
    df = pd.read_excel(input_file)
    df['CAI_<=-25'] = None
    df['CAI_>-25'] = None
    df.loc[df['Minimum Free Energy (80nts)'] <= -25, 'CAI_<=-25'] = df['CAI']
    df.loc[df['Minimum Free Energy (80nts)'] > -25, 'CAI_>-25'] = df['CAI']
    
    result_df = df[['CAI_<=-25', 'CAI_>-25']].dropna(how='all')

    result_df.to_excel(output_file, index=False)

input_file = r"C:\Users\JZQ\Desktop\Research\9col.xlsx"
output_file = r"C:\Users\JZQ\Downloads\80_CAI.xlsx"   
process_excel(input_file, output_file)


