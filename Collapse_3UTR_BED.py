import os
import sys

def collapse_bed(filename):
    """collapse the bedfile to return a dictionary with chromosome, start, stop
as keys and their corresponding transcript ID list, score and signs as values"""
    transcripts = {}
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts)>1:
                key = (parts[0], parts[1], parts[2])
                trans = parts[3].split('_')
                score = parts[4]
                sign = parts[5]
                newTrans = ''
                for p in trans:
                    if p == '0':
                        newTrans += '0'
                        break
                    if p != '0':
                        newTrans += p + "_"
                if key not in transcripts:
                    transcripts[key] = ([newTrans], score, sign)
                else:
                    (trans, score1, sign1) = transcripts[key]
                    trans.append(newTrans)
                    transcripts[key] = (trans, score1, sign1)

    print(transcripts)
    return transcripts

def write_and_sort():
    """
    Write entries for each transcript ID to a separate BED file in the specified
    directory and then sort each resulting BED file.
    """
    data = collapse_bed(r"C:\Users\JZQ\Downloads\Modified_BED.bed")
    out_filename = r"C:\Users\JZQ\Downloads\test.bed"
    for transcript_id, entries in data.items():
        with open(out_filename, 'a') as f:
            f.write(transcript_id[0] + '\t' + transcript_id[1] + '\t' + transcript_id[2] + '\t' + entries[0][0] + '\t' + entries[1] + '\t' + entries[2]+"\n")

# collapse_bed(r"C:\Users\JZQ\Downloads\Modified_BED.bed")
write_and_sort()