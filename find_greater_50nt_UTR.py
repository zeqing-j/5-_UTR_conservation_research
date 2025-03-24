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
            mfe_value = None

            for i, line in enumerate(lines):
                if "MFE Structure" in line:
                    mfe_structure_line = lines[i + 1].strip()
                    mfe_structure = mfe_structure_line.split(' ')[0]
                    mfe_structure = mfe_structure.strip()
                    mfe_structure_length = len(mfe_structure_line)
                    break
                    
            if mfe_structure_line and mfe_structure_length >= 50:
                for line in lines:
                    if "Minimum Free Energy: " in line:
                        mfe_value = re.search(r"Minimum Free Energy: ([-\d.]+) kcal/mol", line)
                        if mfe_value:
                            mfe_value = mfe_value.group(1)
                            break

            if mfe_value:
                result = f"{filename[:-4]}:{mfe_value}"
                results.append(result)

    return results

def main():
    directory = "/ocean/projects/bio200049p/zjiang2/Files/5primedata/bigbed_whole_genome/test_dir"
    output = process_files(directory)
    output_file = "/ocean/projects/bio200049p/zjiang2/Files/5primedata/bigbed_whole_genome/greater50UTR.txt"
    with open(output_file, 'w') as f:
        for item in output:
            f.write(item + "\n")

if __name__ == "__main__":
    main()
