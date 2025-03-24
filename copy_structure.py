import os
import sys
def copy_file(source_file, destination_file):
        with open(source_file, 'r') as source:
            source_lines = source.readlines()

        mfe_structure_index = None
        for i, line in enumerate(source_lines):
            if line.startswith("MFE Structure"):
                mfe_structure_index = i
                break
        
        if mfe_structure_index is not None:
            mfe_structure = ''.join(source_lines[mfe_structure_index + 1:])
            mfe_structure = mfe_structure.split(' ')[0]  
            mfe_structure = mfe_structure.strip()  
            mfe_structure = "#=GC SS_cons " + mfe_structure
            
            with open(destination_file, 'a') as destination:
                destination.write(mfe_structure)
                destination.write('\n')

            print(f"MFE Structure content copied to '{destination_file}' successfully.")
        else:
            print("MFE Structure not found in the source file.")

def main():
    if len(sys.argv) != 3:
        print("Usage: python extract_strand.py <Input directory containing BED files> <Output text file>")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_file = sys.argv[2]
    copy_file(input_directory, output_file)

if __name__ == "__main__":
    main()


from Bio import SeqIO

records = SeqIO.parse("/ocean/projects/bio200049p/smishra1/TTN5p/TTN5p.fasta", "fasta")
count = SeqIO.write(records, "/ocean/projects/bio200049p/smishra1/TTN5p/TTN5p.sto", "stockholm")
print("Converted %i records" % count)
