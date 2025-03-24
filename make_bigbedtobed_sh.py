import os
import sys

def generate_bash_script(chrom, start, end, strand, output_dir):
    script_content = (
        "#!/bin/bash\n"
        "DIR='/ocean/projects/bio200049p/zjiang2/Tools_Installed/ucsc'\n"
        "cd '$DIR'\n"
        f"./bigBedToBed http://hgdownload.soe.ucsc.edu/goldenPath/hg38/multiz470way/multiz470way.bigMaf stdout "
        f"-chrom={chrom} -start={start} -end={end} | cut -f 4 | tr ';' "
        f"'\n' > /ocean/projects/bio200049p/zjiang2/Files/5primedata/test_bigbed/maf_dir/{chrom}_{start}_{end}_{strand}.maf\n"
    )

    script_name = f"{chrom}_{start}_{end}_{strand}.sh"
    script_path = os.path.join(output_dir, script_name)

    with open(script_path, 'w') as script_file:
        script_file.write(script_content)
    os.chmod(script_path, 0o755)

def generate_sh_files(input_dir, output_dir):
    """
    Generate .sh script files for each BED file in the input directory.
    """
    # Ensure the output directory exists or create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    maf_path_prefix = "/ocean/projects/bio200049p/zjiang2/Scripts/OtherBedRun/Othermaf/"
    refTargets_path_prefix = "/ocean/projects/bio200049p/zjiang2/Scripts/OtherBedRun/Other/"
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".bed"):
            with open(filename, 'r') as file:
                for line in file:
                    elements = line.strip().split()
                    chrom = elements[0]
                    start = elements[1]
                    end = elements[2]
                    strand = elements[5]
                    generate_bash_script(chrom, start, end, strand, output_dir)
def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <Input directory containing BED files> <Output directory for .sh files>")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_directory = sys.argv[2]
    generate_sh_files(input_directory, output_directory)

if __name__ == "__main__":
    main()
