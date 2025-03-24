import os
import sys

def find_bed_file_with_condition(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".bed"):
            filepath = os.path.join(directory, filename)
            
            with open(filepath, 'r') as bed_file:
                first_line = bed_file.readline().strip()
                
                elements = first_line.split()
                
                if len(elements) > 1 and elements[1].startswith("17"):
                    print(f"Found matching file: {filename}")
                    return filename  # Return the filename and stop processing

    print("No matching file found.")
    return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <Output folder to write BED files per transcript> <Path to the single large BED file containing details of all transcripts")
        sys.exit(1)

    BED_directory = sys.argv[1]  
    find_bed_file_with_condition(BED_directory)
    

if __name__ == "__main__":
    main()

