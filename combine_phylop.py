
def get_transcript_name(full_name):
    """Extract the transcript name without the number and underscore."""
    return full_name.split('_')[0]

def process_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        previous_transcript = ""
        combined_scores = []

        while True:
            name_line = infile.readline().strip()
            if not name_line:
                # End of file
                break

            score_line = infile.readline().strip()
            current_transcript = get_transcript_name(name_line)
            
            if previous_transcript and current_transcript != previous_transcript:
                # Write the previous transcript name and combined scores to the output file
                outfile.write(previous_transcript + '\n')
                outfile.write(','.join(map(str, combined_scores)) + '\n')
                combined_scores = []

            previous_transcript = current_transcript
            combined_scores.extend(map(float, score_line.split(',')))

        # Write the last transcript if it hasn't been written
        if previous_transcript:
            outfile.write(previous_transcript + '\n')
            outfile.write(','.join(map(str, combined_scores)) + '\n')

    print(f"Processed data has been written to {output_file}")


if __name__ == "__main__":
    input_file = '/ocean/projects/bio200049p/zjiang2/Files/RNAfold/test.txt'
    output_file = '/ocean/projects/bio200049p/zjiang2/Files/RNAfold/testoutput.txt'
    process_file(input_file, output_file)
