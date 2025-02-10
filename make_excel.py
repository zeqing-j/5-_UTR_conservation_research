import os
import sys
import pandas as pd

def calculate_percentage(filepath):
        with open(filepath, 'r') as file:
            source_lines = file.readlines()

        mfe_structure_index = None
        for i, line in enumerate(source_lines):
            if line.startswith("MFE Structure"):
                mfe_structure_index = i
                break
        
        if mfe_structure_index is not None:
            mfe_structure = ''.join(source_lines[mfe_structure_index + 1:])
            mfe_structure = mfe_structure.split(' ')[0]  # Remove numbers at the end
            mfe_structure = mfe_structure.strip()  # Remove leading/trailing whitespaces
            num_open_parentheses = mfe_structure.count('(')
            percentage = (num_open_parentheses / len(mfe_structure)) * 100
            return percentage
        else: return 0

def process_files(input_dir, output_txt, output_excel):
    result_dict = {}
    for filename in os.listdir(input_dir):
        if filename.endswith('.txt'):
            new_file_list = filename.split(".")
            new_file = new_file_list[0] + "." + new_file_list[1]
            file_path = os.path.join(input_dir, filename)
            percentage = calculate_percentage(file_path)
            result_dict[new_file] = percentage
    
    # Write to text file
    with open(output_txt, 'w') as txt_file:
        for filename, percentage in result_dict.items():
            txt_file.write(f"{filename}:{percentage:.2f}%\n")
    
    # Write to Excel file
    df = pd.DataFrame(list(result_dict.items()), columns=['Filename', 'Percentage'])
    df.to_excel(output_excel, index=False)

def main():
    if len(sys.argv) != 4:
        print("Usage: python make_excel.py <Input .txt file> <rscape directory> <Output directory>")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_txt = sys.argv[2]
    output_excel = sys.argv[3]
    process_files(input_dir, output_txt, output_excel)

if __name__ == "__main__":
    main()

