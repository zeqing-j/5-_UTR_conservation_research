import os
import sys

def create_config(input_directory, output_filename, num_scripts=38591):
    """
    Generate a config file that calls the first num_scripts .sh files using their full paths.
    """
    # Define the full path prefix
    path_prefix = "/ocean/projects/bio200049p/zjiang2/Files/5primedata/test_bigbed/bash_dir/"

    # List all .sh files in the input directory
    sh_files = [f for f in os.listdir(input_directory) if f.endswith(".sh")]

    # Sort the list to ensure consistent order
    sh_files.sort()

    # Take only the first num_scripts
    selected_files = sh_files[:num_scripts]

    # Create the config file content
    with open(output_filename, 'w') as f:
        for i,j in enumerate(selected_files):
            f.write(f"bash {path_prefix}{j}\n")

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <Directory containing .sh scripts> <Output config_file.txt path>")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_filename = sys.argv[2]
    create_config(input_directory, output_filename)

if __name__ == "__main__":
    main()

