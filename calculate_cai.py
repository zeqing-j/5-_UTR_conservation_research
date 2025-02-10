from collections import defaultdict
import math

# Step 1: Human codon usage table
codon_usage = {
    'UUU': 17.6, 'UCU': 15.2, 'UAU': 12.2, 'UGU': 10.6,
    'UUC': 20.3, 'UCC': 17.7, 'UAC': 15.3, 'UGC': 12.6,
    'UUA': 7.7, 'UCA': 12.2, 'UAA': 1.0, 'UGA': 1.6,
    'UUG': 12.9, 'UCG': 4.4, 'UAG': 0.8, 'UGG': 13.2,
    'CUU': 13.2, 'CCU': 17.5, 'CAU': 10.9, 'CGU': 4.5,
    'CUC': 19.6, 'CCC': 19.8, 'CAC': 15.1, 'CGC': 10.4,
    'CUA': 7.2, 'CCA': 16.9, 'CAA': 12.3, 'CGA': 6.2,
    'CUG': 39.6, 'CCG': 6.9, 'CAG': 34.2, 'CGG': 11.4,
    'AUU': 16.0, 'ACU': 13.1, 'AAU': 17.0, 'AGU': 12.1,
    'AUC': 20.8, 'ACC': 18.9, 'AAC': 19.1, 'AGC': 19.5,
    'AUA': 7.5, 'ACA': 15.1, 'AAA': 24.4, 'AGA': 12.2,
    'AUG': 22.0, 'ACG': 6.1, 'AAG': 31.9, 'AGG': 12.0,
    'GUU': 11.0, 'GCU': 18.4, 'GAU': 21.8, 'GGU': 10.8,
    'GUC': 14.5, 'GCC': 27.7, 'GAC': 25.1, 'GGC': 22.2,
    'GUA': 7.1, 'GCA': 15.8, 'GAA': 29.0, 'GGA': 16.5,
    'GUG': 28.1, 'GCG': 7.4, 'GAG': 39.6, 'GGG': 16.5
}

# Step 2: Calculate relative adaptiveness (w) for each codon
w_values = {}
codon_table = {
    'F': ['UUU', 'UUC'], 'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
    'I': ['AUU', 'AUC', 'AUA'], 'M': ['AUG'], 'V': ['GUU', 'GUC', 'GUA', 'GUG'],
    'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'], 'P': ['CCU', 'CCC', 'CCA', 'CCG'],
    'T': ['ACU', 'ACC', 'ACA', 'ACG'], 'A': ['GCU', 'GCC', 'GCA', 'GCG'],
    'Y': ['UAU', 'UAC'], 'H': ['CAU', 'CAC'], 'Q': ['CAA', 'CAG'],
    'N': ['AAU', 'AAC'], 'K': ['AAA', 'AAG'], 'D': ['GAU', 'GAC'],
    'E': ['GAA', 'GAG'], 'C': ['UGU', 'UGC'], 'W': ['UGG'],
    'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 'G': ['GGU', 'GGC', 'GGA', 'GGG'],
    'Stop': ['UAA', 'UGA', 'UAG']
}

# Calculate RSCU values
rscu_values = defaultdict(dict)
for aa, codons in codon_table.items():
    for codon in codons:
        rscu_values[aa][codon] = codon_usage[codon]

# Calculate w values
for aa, codons in rscu_values.items():
    max_rscu = max(codons.values())
    for codon, rscu in codons.items():
        w_values[codon] = rscu / max_rscu
        print(f"{codon}: {w_values[codon]}")

# Step 3: Calculate CAI
def calculate_cai(sequence):
    cai = 1.0
    codon_count = 0

    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i + 3]
        if codon in w_values:
            cai *= w_values[codon]
            codon_count += 1

    if codon_count > 0:
        cai = pow(cai, 1 / codon_count)
    else:
        cai = 0.0

    return cai

# Step 4: Process input file and write to output file
def process_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        lines = infile.readlines()
        for i in range(0, len(lines), 2):
            name = lines[i].strip()
            sequence = lines[i + 1].strip().replace('T', 'U')  # Replace T with U for RNA
            cai = calculate_cai(sequence)
            outfile.write(f"{name}\n{cai}\n")


def main():
        # input_file = '/ocean/projects/bio200049p/zjiang2/Files/RNAfold/v33_CDS.fasta'
        # output_file = '/ocean/projects/bio200049p/zjiang2/Files/RNAfold/v33_CAI.fasta'
        # process_file(input_file, output_file)
        sequence = "ATGAACCACTCGCCGCTCAAGACCGCCTTGGCGTACGAATGCTTCCAGGACCAGGACAAC"
        sequence1 = sequence.replace('T', 'U')
        calculate_cai(sequence1) #TCCACGTTGGCTTTGCCGTCGGACCAAAAGATGAAAACAGGCACGTCTGGCAGGCAGCGCGTGCAGGAGCAGGTGATGATGACCGTCAAGCGGCAGAAGTCCAAGTCTTCCCAGTCGTCCACCCTGAGCCACTCCAATCGAGGTTCCATGTATGATGGCTTGGCTGACAATTACAACTATGGGACCACCAGCAGGAGCAGCTACTACTCCAAGTTCCAGGCAGGGAATGGCTCATGGGGATATCCGATCTACAATGGAACCCTCAAGCGGGAGCCTGACAACAGGCGCTTCAGCTCCTACAGCCAGATGGAGAACTGGAGCCGGCACTACCCCCGGGGCAGCTGTAACACCACCGGCGCAGGCAGCGACATCTGCTTCATGCAGAAAATCAAGGCGAGCCGCAGTGAGCCCGACCTCTACTGTGACCCACGGGGCACCCTGCGCAAGGGCACGCTGGGCAGCAAGGGCCAGAAGACCACCCAGAACCGCTACAGCTTTTACAGCACCTGCAGTGGTCAGAAGGCCATAAAGAAGTGCCCTGTGCGCCCGCCCTCTTGTGCCTCCAAGCAGGACCCTGTGTATATCCCGCCCATCTCCTGCAACAAGGACCTGTCCTTTGGCCACTCTAGGGCCAGCTCCAAGATCTGCAGTGAGGACATCGAGTGCAGTGGGCTGACCATCCCCAAGGCTGTGCAGTACCTGAGCTCCCAGGATGAGAAGTACCAGGCCATTGGGGCCTATTACATCCAGCATACCTGCTTCCAGGATGAATCTGCCAAGCAACAGGTCTATCAGCTGGGAGGCATCTGCAAGCTGGTGGACCTCCTCCGCAGCCCCAACCAGAACGTCCAGCAGGCCGCGGCAGGGGCCCTGCGCAACCTGGTGTTCAGGAGCACCACCAACAAGCTGGAGACCCGGAGGCAGAATGGGATCCGCGAGGCAGTCAGCCTCCTGAGGAGAACCGGGAACGCCGAGATCCAGAAGCAGCTGACTGGGCTGCTCTGGAACCTGTCTTCCACTGACGAGCTGAAGGAGGAACTCATTGCCGACGCCCTGCCTGTTCTGGCCGACCGCGTCATCATTCCCTTCTCTGGCTGGTGCGATGGCAATAGCAACATGTCCCGGGAAGTGGTGGACCCTGAGGTCTTCTTCAATGCCACAGGCTGCTTGAGAAAGAGACTGGGCATGCGGGAGCTTCTGGCTCTTGTTCCGCAAAGGGCCACTAGTAGCAGGGTGAACCTGAGCTCGGCCGATGCAGGCCGCCAGACCATGCGTAACTACTCAGGGCTCATTGATTCCCTCATGGCCTATGTCCAGAACTGTGTAGCGGCCAGCCGCTGTGACGACAAGTCTGTGGAAAACTGCATGTGTGTTCTGCACAACCTCTCCTACCGCCTGGACGCCGAGGTGCCCACCCGCTACCGCCAGCTGGAGTATAACGCCCGCAACGCCTACACCGAGAAGTCCTCCACTGGCTGCTTCAGCAACAAGAGCGACAAGATGATGAACAACAACTATGACTGCCCCCTGCCTGAGGAAGAGACCAACCCCAAGGGCAGCGGCTGGTTGTACCATTCAGATGCCATCCGCACCTACCTGAACCTCATGGGCAAGAGCAAGAAAGATGCTACCCTGGAGGCCTGTGCTGGTGCCCTGCAGAACCTGACAGCCAGCAAGGGGCTGATGTCCAGTGGCATGAGCCAGTTGATTGGGCTGAAGGAAAAGGGCCTGCCACAAATTGCCCGCCTCCTGCAATCTGGCAACTCTGATGTGGTGCGGTCCGGAGCCTCCCTCCTGAGCAACATGTCCCGCCACCCTCTGCTGCACAGAGTGATGGGGAACCAGGTGTTCCCGGAGGTGACCAGGCTCCTCACCAGCCACACTGGCAATACCAGCAACTCCGAAGACATCTTGTCCTCGGCCTGCTACACTGTGAGGAACCTGATGGCCTCGCAGCCACAACTGGCCAAGCAGTACTTCTCCAGCAGCATGCTCAACAACATCATCAACCTGTGCCGAAGCAGTGCCTCACCCAAGGCCGCAGAAGCTGCCCGGCTTCTCCTGTCTGACATGTGGTCCAGCAAGGAACTGCAGGGTGTCCTCAGACAGCAAGGTTTCGATAGGAACATGCTGGGAACCTTAGCTGGGGCCAACAGCCTCAGGAACTTCACCTCCCGATTCTAA"

if __name__ == "__main__":
    main()



