import os
import re
from collections import defaultdict

def extract_file_info(filename):
    # Define the regex pattern for extracting the file info
    pattern = r'(?P<transcript_id>[^_]+)_(?P<chr>[^_]+)_(?P<start>\d+)_(?P<end>\d+)_(?P<strand>[+-])\.maf$'
    match = re.match(pattern, filename)
    
    if match:
        return match.groupdict()
    return None

def combine_maf_files(input_dir, output_dir):
    # Create a dictionary to group files by transcript_id and strand
    grouped_files = defaultdict(list)

    # Traverse the input directory
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".maf"):
                info = extract_file_info(file)
                if info:
                    key = (info['transcript_id'], info['strand'])
                    grouped_files[key].append((int(info['start']), file))
    
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Process each group of files
    for (transcript_id, strand), files in grouped_files.items():
        # Sort files by the start position
        sorted_files = sorted(files)

        # Create the output file name
        output_filename = f"{transcript_id}_{strand}.maf"
        output_filepath = os.path.join(output_dir, output_filename)

        with open(output_filepath, 'w') as output_file:
            for _, filename in sorted_files:
                input_filepath = os.path.join(input_dir, filename)
                with open(input_filepath, 'r') as input_file:
                    output_file.write(input_file.read())


def main():
    input_directory = "/ocean/projects/bio200049p/zjiang2/Files/5primedata/test_bigbed/new_fixed_maf_dir"
    output_directory = "/ocean/projects/bio200049p/zjiang2/Files/5primedata/test_bigbed/final_maf_dir"
    combine_maf_files(input_directory, output_directory)

    print(f"Modified MAF files have been saved in {output_directory}")

if __name__ == "__main__":
    main()