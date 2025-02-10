import os
import sys

def generate_sh_files(input_directory, output_directory):
    """
    Generate .sh script files for each BED file in the input directory.
    """
    # Ensure the output directory exists or create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    maf_path_prefix = "/ocean/projects/bio200049p/zjiang2/Scripts/OtherBedRun/Othermaf/"
    refTargets_path_prefix = "/ocean/projects/bio200049p/zjiang2/Scripts/OtherBedRun/Other/"

    # Iterate over all files in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".bed"):
            base_name = os.path.splitext(filename)[0] 
            # Construct the .sh script content
            script_content = (
                "#!/bin/bash\n"
                f"/ocean/projects/bio200049p/smishra1/repos/hal/bin/hal2maf /ocean/projects/bio200049p/smishra1/Files/241-mammalian-2020v2.hal "
                f"{maf_path_prefix}{base_name}.maf "
                f"--refTargets {refTargets_path_prefix}{base_name}.bed "
                "--noAncestors --refGenome Homo_sapiens --maxRefGap 10\n"
            )

            # Define the output .sh filename
            output_filename = os.path.join(output_directory, f"{filename}.sh")

            # Write the script content to the .sh file
            with open(output_filename, 'w') as f:
                f.write(script_content)
            # Make the .sh file executable
            os.chmod(output_filename, 0o755)

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <Input directory containing BED files> <Output directory for .sh files>")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_directory = sys.argv[2]
    generate_sh_files(input_directory, output_directory)

if __name__ == "__main__":
    main()

