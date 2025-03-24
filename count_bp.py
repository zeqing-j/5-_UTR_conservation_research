import os
import sys
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
            mfe_structure = mfe_structure.split(' ')[0] 
            mfe_structure = mfe_structure.strip()  
            num_open_parentheses = mfe_structure.count('(')
            percentage = (num_open_parentheses / len(mfe_structure)) * 100
        return percentage

def process_directory(directory):
    percent_pair = {}
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            new_file_list = filename.split(".")
            new_file = new_file_list[0] + "." + new_file_list[1]
            file_path = os.path.join(directory, filename)
            percentage = calculate_percentage(file_path, filename)
            percent_pair[new_file] = percentage
    return percent_pair

def write_to_file(percent_pair, output_file):
    with open(output_file, 'w') as file:
        for filename, percentage in percent_pair.items():
            file.write(f"{filename}: {percentage:.2f}%\n")

def main():
    if len(sys.argv) != 3:
        print("Usage: python extract_strand.py <Input directory containing .txt files> <Output text file>")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_file = sys.argv[2]
    percent_pair = process_directory(input_directory)
    write_to_file(percent_pair, output_file)
    print("Output written to percentPair.txt")

if __name__ == "__main__":
    main()
