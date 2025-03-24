import os
import sys

def make_bed(chromosome_dir, chromosome_number, score, sign, output_dir):
    min_position = float('inf')  
    max_position = float('-inf') 

    bed_files = [f for f in os.listdir(chromosome_dir) if f.endswith('.bed')]

    for bed_file in bed_files:
        bed_file_path = os.path.join(chromosome_dir, bed_file)
        with open(bed_file_path, 'r') as f:
            for line in f:
                parts = line.strip().split('\t')
                if len(parts) < 6:
                    continue  
                start = int(parts[1]) 
                end = int(parts[2]) 
                min_position = min(min_position, start)
                max_position = max(max_position, end)

    strand = '+' if sign == 'plus' else '-'
    
    output_filename = f"{chromosome_number}_{sign}.bed"
    output_bed_path = os.path.join(output_dir, output_filename)
    with open(output_bed_path, 'w') as out_file:
        output_line = f"{chromosome_number}\t{min_position}\t{max_position}\t{chromosome_number}_{sign}\t{score}\t{strand}\n"
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
