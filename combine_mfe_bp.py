def read_file(file_path):
    data = {}
    with open(file_path, 'r') as file:
        for line in file:
            if ':' in line:
                name, number = line.strip().split(':', 1)
                data[name] = number
    return data

def find_common_entries(file1_data, file2_data):
    common_entries = {}
    for name in file1_data:
        if name in file2_data:
            common_entries[name] = f"{file1_data[name]};{file2_data[name]}"
    return common_entries

def write_common_entries(output_file, common_entries):
    with open(output_file, 'w') as file:
        for name, numbers in common_entries.items():
            file.write(f"{name}:{numbers}\n")

def main():
    file1_path = "/ocean/projects/bio200049p/zjiang2/Files/5primedata/bigbed_whole_genome/greater50UTR.txt"
    file2_path = "/ocean/projects/bio200049p/zjiang2/Files/5primedata/bigbed_whole_genome/bp_percentage.txt"

    file1_data = read_file(file1_path)
    file2_data = read_file(file2_path)

    common_entries = find_common_entries(file1_data, file2_data)

    output_file = "/ocean/projects/bio200049p/zjiang2/Files/5primedata/bigbed_whole_genome/common_results.txt"
    write_common_entries(output_file, common_entries)

    print(f"Common entries saved to {output_file}")

if __name__ == "__main__":
    main()
