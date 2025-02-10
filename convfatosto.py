from Bio import SeqIO

records = SeqIO.parse("/ocean/projects/bio200049p/zjiang2/Files/ttn_cactus/ENST00000589042.5.fasta", "fasta")
count = SeqIO.write(records, "/ocean/projects/bio200049p/zjiang2/Files/ttn_cactus/ENST00000589042.5.sto", "stockholm")
print("Converted %i records" % count)
