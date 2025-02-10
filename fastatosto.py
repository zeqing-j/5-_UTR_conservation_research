import os
import sys
from Bio import SeqIO

def copy_file(destination_file, source_file):
        mfe_structure = ''
        with open(source_file, 'r') as source:
            source_lines = source.readlines()

        mfe_structure_index = None
        for i, line in enumerate(source_lines):
            if line.startswith("MFE Structure"):
                mfe_structure_index = i
                break

        if mfe_structure_index is not None:
            mfe_structure = ''.join(source_lines[mfe_structure_index + 1:])
            mfe_structure = mfe_structure.split(' ')[0]  # Remove numbers at the end
            mfe_structure = mfe_structure.strip()  # Remove leading/trailing whitespaces
            mfe_structure = "#=GC SS_cons " + mfe_structure + "\n"

        with open(destination_file, 'r') as dest:
            dest_content = dest.readlines()

        updated_content = dest_content[:-1]  # Exclude the last two lines

        updated_content.append(mfe_structure)
        updated_content.extend(dest_content[-1:])  # Add back the last two lines

        # Write the updated content back to the destination file
        with open(destination_file, 'w') as dest:
            dest.writelines(updated_content)

def find_file(directory, filename):
    # Search for the file in the directory
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return True

    print(f"File '{filename}' not found in directory '{directory}'.")
    return False

def fastatosto(dir1, dir2):
    files_in_dir1 = os.listdir(dir1)
    #print(files_in_dir1)
    for filename in files_in_dir1:
        new_file_list = filename.split(".")
        new_file = new_file_list[0] + "." + new_file_list[1]
        fasta_dir = "/ocean/projects/bio200049p/zjiang2/Files/test_dir_1"
        fasta = f"fasta_dir + "/" + {new_file}.fasta"
        records = SeqIO.parse(fasta, "fasta")
        out_filename = os.path.join(dir2, f"{new_file}.sto")   
        count = SeqIO.write(records, out_filename, "stockholm")
        print("Converted %i records" % count)
        destination_file = dir2 + "/" + out_filename
        copy_file(destination_file, filename)


def main():
    if len(sys.argv) != 3:
        print("Usage: python extract_strand.py <Input directory containing BED files> <Output text file>")
        sys.exit(1)

    struc_directory= sys.argv[1]
    sto_directory = sys.argv[2]
    fastatosto(struc_directory,sto_directory)

if __name__ == "__main__":
    main()