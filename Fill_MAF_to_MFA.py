import os

def generate_bash_script(maf_dir, strands_file, bash_script_name):
    # Read strands from Strands.txt
    strands = {}
    with open(strands_file, 'r') as sf:
        for line in sf:
            transcript_id, strand = line.strip().split(':')
            strands[transcript_id] = strand

    # Generate commands
    commands = []
    #print(strands)
    for filename in os.listdir(maf_dir):
        if filename.endswith(".maf"):
            transcript_id = ".".join(filename.split(".")[:-1])
           # print(transcript_id)
            
            if transcript_id in strands:
                input_maf = os.path.join(maf_dir, filename)
                outdir='/ocean/projects/bio200049p/zjiang2/Scripts/OtherBedRun/Otherfasta/'
                output_fasta = os.path.join(outdir, transcript_id + ".fasta")
                cmd = f"python /ocean/projects/bio200049p/smishra1/Scripts/New_Concatenate_Seq_General_3p.py {input_maf} {output_fasta} {strands[transcript_id]} 0 0"
                commands.append(cmd)

    # Write commands to bash script
    with open(bash_script_name, 'w') as bf:
        #bf.write("#!/bin/bash\n")
        for cmd in commands:
            bf.write(cmd + "\n")
    
    # Make the bash script executable
    os.chmod(bash_script_name, 0o755)

maf_directory = "/ocean/projects/bio200049p/zjiang2/Scripts/OtherBedRun/Othermaf"
strands_filename = "/ocean/projects/bio200049p/zjiang2/Scripts/OtherBedRun/Strand.txt"
output_txt_script = "/ocean/projects/bio200049p/zjiang2/Scripts/OtherBedRun/maf_to_fasta_commands.txt"

generate_bash_script(maf_directory, strands_filename, output_txt_script)

