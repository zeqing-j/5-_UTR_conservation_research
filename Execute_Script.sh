#!/bin/bash
#SBATCH -t 72:00:00
#SBATCH -p RM-shared
#SBATCH -N 1
#SBATCH --ntasks-per-node=64

# Directory containing FASTA files
FASTA_DIR="/ocean/projects/bio200049p/zjiang2/Files/spring24/filteredfasta"
# Directory where the linearalifold binary is located
LAF_DIR="/ocean/projects/bio200049p/smishra1/Files/LinearAlifold-main"
# Output directory for the results
OUTPUT_DIR="/ocean/projects/bio200049p/zjiang2/Files/spring24/newstruc"

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Navigate to the linearalifold directory
cd "$LAF_DIR"

# Loop through each FASTA file in the FASTA_DIR
for fasta_file in "$FASTA_DIR"/*.txt; do
    # Extract the filename without the extension for output naming
    base_name=$(basename "$fasta_file" .txt)

    # Construct the output file path
    output_file="${OUTPUT_DIR}/${base_name}.txt"

    if [ -f "$output_file" ]; then
       echo "Output file exists, skipping: $output_file"

    else
    # Run the command and redirect output to the output file
       cat "$fasta_file" | ./linearalifold.py > "$output_file"
       echo "Processed: $fasta_file"
    fi
done

