import os
import shutil
import sys

def copy_matching_files(rscape_directory, sto_directory, output_directory):
    # Get list of transcript ids from rscape_directory
    transcript_ids = os.listdir(rscape_directory)
    
    # Iterate through sto_directory
    for sto_file in os.listdir(sto_directory):
        # Check if sto file starts with a transcript id
        for transcript_id in transcript_ids:
            if sto_file.startswith(transcript_id):
                # If match found, copy sto file to output directory
                sto_file_path = os.path.join(sto_directory, sto_file)
                output_file_path = os.path.join(output_directory, sto_file)
                shutil.copy(sto_file_path, output_file_path)
                print(f"copied {transcript_id} into sto_threshold")
                break


def main():
    if len(sys.argv) != 4:
        print("Usage: python extract_strand.py <Input directory containing BED files> <Output text file>")
        sys.exit(1)

    rscape_directory = sys.argv[1]
    sto_directory = sys.argv[2]
    output = sys.argv[3]

    copy_matching_files(rscape_directory, sto_directory, output)

if __name__ == "__main__":
    main()



import os
import shutil
import sys

def copy_missing_files(directory1, directory2, directory3):
    # Get a list of all bed files in directory 1
    bed_files_directory1 = [f for f in os.listdir(directory1) if f.endswith('.bed')]

    # Get a list of all maf files in directory 2
    maf_files_directory2 = [f for f in os.listdir(directory2) if f.endswith('.maf')]

    # Extract the base names of maf files (without extension)
    maf_file_names = [os.path.splitext(f)[0] for f in maf_files_directory2]

    # Iterate over bed files in directory 1
    for bed_file in bed_files_directory1:
        # Extract base name of bed file (without extension)
        bed_base_name = os.path.splitext(bed_file)[0]

        # Check if bed base name exists in maf files
        if bed_base_name not in maf_file_names:
            # If not, copy the bed file to directory 3
            shutil.copy(os.path.join(directory1, bed_file), os.path.join(directory3, bed_file))
            print(f"Copied {bed_file} to {directory3}")