import os
import sys

def extract_strand_info(input_directory, output_file):
    """
    Extract strand information from each BED file in the input directory
    and save the data to a text file.
    """
    strand_data = {}  # Dictionary to store strand information

    # Iterate over all files in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".bed"):
            base_name = os.path.splitext(filename)[0]

            # Extract strand information from the BED file
            with open(os.path.join(input_directory, filename), 'r') as bed_file:
                line = bed_file.readline().strip()
                fields = line.split('\t')
                if len(fields) > 5:  # Ensure we have the strand column
                    strand = fields[5]
                    strand_data[base_name] = strand  # Store the strand information

    # Save the extracted strand data as a text file
    with open(output_file, 'w') as txt_file:
        for file_base, strand in strand_data.items():
            txt_file.write(f"{file_base}: {strand}\n")

def main():
    if len(sys.argv) != 3:
        print("Usage: python extract_strand.py <Input directory containing BED files> <Output text file>")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_file = sys.argv[2]
    extract_strand_info(input_directory, output_file)

if __name__ == "__main__":
    main()

