import os
import sys

def make_bed(chromosome_dir, chromosome_number, score, sign, output_dir):
    # Initialize minimum and maximum positions
    min_position = float('inf')  # Smallest position in the second column
    max_position = float('-inf')  # Largest position in the third column

    # Read all BED files in the "chromosome" directory
    bed_files = [f for f in os.listdir(chromosome_dir) if f.endswith('.bed')]

    # Iterate over each BED file
    for bed_file in bed_files:
        bed_file_path = os.path.join(chromosome_dir, bed_file)
        with open(bed_file_path, 'r') as f:
            # Iterate over each line in the BED file
            for line in f:
                parts = line.strip().split('\t')
                if len(parts) < 6:
                    continue  # Skip if the line does not have enough columns
                start = int(parts[1])  # Second element (start position)
                end = int(parts[2])  # Third element (end position)
                # Update min and max positions
                min_position = min(min_position, start)
                max_position = max(max_position, end)

    # Determine the correct strand based on the sign input
    strand = '+' if sign == 'plus' else '-'

    # Create the output BED file with one line
    output_filename = f"{chromosome_number}_{sign}.bed"
    output_bed_path = os.path.join(output_dir, output_filename)
    with open(output_bed_path, 'w') as out_file:
        # Construct the output line
        output_line = f"{chromosome_number}\t{min_position}\t{max_position}\t{chromosome_number}_{sign}\t{score}\t{strand}\n"
        # Write the output line to the new BED file
        out_file.write(output_line)

    print(f"Created output BED file: {output_bed_path}")

def main():
    if len(sys.argv) != 6:
        print("Usage: python script.py <Output folder to write BED files per transcript> <Path to the single large BED file containing details of all transcripts")
        sys.exit(1)

    BED_directory = sys.argv[1]  #/ocean/projects/bio200049p/zjiang2/Files/5primedata/parsed_BED/chr1
    number = sys.argv[2]
    score = sys.argv[3]
    sign = sys.argv[4]
    outputfile = sys.argv[5]
    make_bed(BED_directory, number, score, sign, outputfile)
    
if __name__ == "__main__":
    main()