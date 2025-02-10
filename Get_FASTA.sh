#!/bin/bash

# Path to the file containing commands
COMMANDS_FILE="/ocean/projects/bio200049p/zjiang2/Scripts/OtherBedRun/maf_to_fasta_commands.txt"

# Execute each command in the file
while IFS= read -r line
do
  $line
done < "$COMMANDS_FILE"
