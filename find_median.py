import pandas as pd

def process_excel(input_file, output_file):
    # Load the Excel file
    df = pd.read_excel(input_file)
    
    # Initialize new columns
    df['CAI_<=-25'] = None
    df['CAI_>-25'] = None

    # Process the rows based on the "Minimum Free Energy (80nts)" column
    df.loc[df['Minimum Free Energy (80nts)'] <= -25, 'CAI_<=-25'] = df['CAI']
    df.loc[df['Minimum Free Energy (80nts)'] > -25, 'CAI_>-25'] = df['CAI']
    
    # Remove empty rows in the new columns
    result_df = df[['CAI_<=-25', 'CAI_>-25']].dropna(how='all')

    # Write the result to a new Excel file
    result_df.to_excel(output_file, index=False)

# Example usage
input_file = r"C:\Users\JZQ\Desktop\Research\9col.xlsx"  # Replace with your input file path
output_file = r"C:\Users\JZQ\Downloads\80_CAI.xlsx"     # Replace with your desired output file path
process_excel(input_file, output_file)


