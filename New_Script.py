import os
import re
import pandas as pd

def parse_sto_file(file_path):
    human_sequence = ""
    secondary_structure = ""
    with open(file_path, 'r') as file:
        lines = file.readlines()
        sequence_lines = [line for line in lines if 'hg38' in line]
        
        if sequence_lines:
            # Assumes the human sequence is on the next line of the header; concatenate if split across multiple lines
            human_sequence = ''.join(sequence_lines).split()[1]
            #print(human_sequence)
            #human_sequence = human_sequence.replace('-', '')  # Remove gaps

        ss_lines = [line for line in lines if line.startswith("#=GC SS_cons")]
        if ss_lines:
            secondary_structure = ss_lines[0].split()[2]
            
    return human_sequence, secondary_structure

def parse_output_txt(file_path):
    with open(file_path) as f:
        content = f.read()

    # Initialize dictionary to store parsed information
    bpairs_info = {}
    # Example regex patterns from the previous implementation
    bpair_pattern = re.compile(r'# BPAIRS (\d+)')
    avg_subs_pattern = re.compile(r'# avg substitutions per BP\s+(\d+\.\d+)')
    expected_covary_pattern = re.compile(r'# BPAIRS expected to covary (\d+\.\d+) \+/\- (\d+\.\d+)')
    observed_covary_pattern = re.compile(r'# BPAIRS observed to covary (\d+)')
    power_analysis_pattern = re.compile(r'\s+\d+\s+\d+\s+\d+\s+(\d+\.\d+)')

    # Extracting BPAIRS information
    for pattern, key in [(bpair_pattern, 'BPAIRS'), 
                         (avg_subs_pattern, 'avg_subs_per_BP'), 
                         (expected_covary_pattern, 'expected_to_covary'), 
                         (observed_covary_pattern, 'observed_to_covary')]:
        match = pattern.search(content)
        if match:
            bpairs_info[key] = match.group(1) if len(match.groups()) == 1 else match.groups()

    # Update for the power analysis
    power_values = [float(match.group(1)) for match in re.finditer(power_analysis_pattern, content)]
    bpairs_info['power_above_0.5_count'] = sum(value > 0.5 for value in power_values)

    return bpairs_info

def main():
    base_dir = "/ocean/projects/bio200049p/zjiang2/Files/5primedata/bigbed_whole_genome/sto_dir"
    results = []
    sto_files = [f for f in os.listdir(base_dir) if f.endswith(".sto")]

    for folder_name,sto in zip(os.listdir(base_dir),sto_files):
    
        #folder_path = os.path.join(base_dir, folder_name)
       # print(folder_path)
        #if os.path.isdir(folder_path):
        #sto_files = [f for f in os.listdir(base_dir) if f.endswith(".sto")]
        output_txt_path = os.path.join("/ocean/projects/bio200049p/zjiang2/Files/5primedata/bigbed_whole_genome/filterrscape_dir/"+folder_name[:-4]+"/", "output.txt")
       # print(output_txt_path)
        bpairs_info = {}
       # print(sto_files)
        
                # Assuming there's only one .sto file per folder for simplicity
        human_sequence, secondary_structure = parse_sto_file(os.path.join(base_dir, sto))

           # print(bpairs_info)
        bpairs_info['secondary_structure'] = secondary_structure

        if os.path.exists(output_txt_path):
            bpairs_info.update(parse_output_txt(output_txt_path))

        if bpairs_info:  # Ensure there's something to report
            transcript = folder_name.split('_')[0]
            bpairs_info['transcript_id'] = transcript
            results.append(bpairs_info)
           # print(results)

    #for result in results:
        
        #print(result)
    if results:
        # Convert the list of dictionaries to a pandas DataFrame
        df = pd.DataFrame(results)

        # Specify your desired output Excel file path
        output_file_path = "/ocean/projects/bio200049p/zjiang2/Files/5primedata/bigbed_whole_genome/RScape_Analysis2.xlsx"
        
        # Write the DataFrame to an Excel file
        # Note: This requires the openpyxl library for .xlsx support
        df.to_excel(output_file_path, index=False)
if __name__ == "__main__":
    main()

