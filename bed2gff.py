import sys

def bed_to_gff(bed_file, gff_file):
    with open(bed_file, 'r') as bed, open(gff_file, 'w') as gff:
        for line in bed:
            if line.strip():  # skip empty lines
                fields = line.strip().split('\t')
                
                # BED fields
                chromosome = fields[0]
                start = int(fields[1]) + 1  # Convert to 1-based start for GFF
                end = fields[2]
                name = fields[3]
                score = fields[4]
                strand = fields[5]
                
                # GFF fields
                source = "bed2gff"
                feature = name
                frame = "."
                
                # Parse ID and Parent from name
                name_parts = name.split('_')
                parent = '_'.join(name_parts[:1])
                
                group = f"ID={name};Parent={parent}"
                
                # Create GFF line
                gff_line = f"{chromosome}\t{source}\t{feature}\t{start}\t{end}\t{score}\t{strand}\t{frame}\t{group}\n"
                gff.write(gff_line)
    print("BED file is converted into gff file")

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <Output folder to write BED files per transcript> <Path to the single large BED file containing details of all transcripts")
        sys.exit(1)

    BED_directory = sys.argv[1]  
    output_directory = sys.argv[2]
    bed_to_gff(BED_directory, output_directory)
    

if __name__ == "__main__":
    main()
