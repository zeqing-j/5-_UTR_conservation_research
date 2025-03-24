import os
import re

def process_files(directory):
    results = []

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                lines = file.readlines()

            mfe_structure_line = None

            for i, line in enumerate(lines):
                if "MFE Structure" in line:
                    mfe_structure_line = lines[i + 1].strip()
                    mfe_structure = mfe_structure_line.split(' ')[0] 
                    mfe_structure = mfe_structure.strip()
                    mfe_structure_length = len(mfe_structure_line)
                    break
            
            if mfe_structure_line:
                result = f"{filename[:-4]}:{mfe_structure_length}"
                results.append(result)


def main():
    directory = "/ocean/projects/bio200049p/zjiang2/Files/5primedata/bigbed_whole_genome/struc_dir"
    output = process_files(directory)
    output_file = "/ocean/projects/bio200049p/zjiang2/Files/5primedata/bigbed_whole_genome/validate50nt.txt"
    with open(output_file, 'w') as f:
        for item in output:
            f.write(item + "\n")

if __name__ == "__main__":
    main()
