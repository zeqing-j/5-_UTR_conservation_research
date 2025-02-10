# 5'UTR conservation research

Data Base: A HAL formatted 240 mammalian whole genome alignments made from the Zoonomia Project (Zoonomia Consortium, 2020) is used to obtain the genome alignment. The UTR coordinates of mammalian genomes are downloaded from the UCSC Genome Browser as Browser Extensible Data (BED) files. 

Methods: Hal2maf is a tool that takes BED coordinates of genome and HAL genome alignment and converts all of the information into a multiple alignment format (MAF). The MAF files contain blocks of alignments of UTRs for all 240 mammalian genomes from the HAL file. After obtaining MAF format files, a script is generated to modify the format of MAF files to multi-FASTA format, which combines each block of alignment for each species to make a whole UTR alignment for each species. A secondary structure prediction in dot and bracket versions can be obtained by running FASTA files in Linearalifold, which is an efficient tool that identifies conserved structures of compensatory mutations in the alignments. Finally, the R-scape program validates the conserved covariation pairs by providing p-values and the power of conserved base pairs.

1.	Make bash file for hal2maf  Create_Conv_Scripts_Per_Trcpt.py
2.	Run bash file to run hal2maf  otherScripts/Rundirectory.sh
3.	Generate each strand (+/-) using Extract_Strand.py (for maf2fasta)
4.	Make bash file for maf2fasta :Make_FASTA/Fill_ MAF_to_MFA.py => maf_to_fasta_commands.txt
5.	Run bash for fasta: bash Get_FASTA.sh 
6.	Call linear alifold  Execute_Script.sh
7.	sbatch call_fastatosto.sh => make fasta to sto and copy structures to sto file with bash
8.	Sbatch Rscape.sh => run rscape on stockhom files
9.	New_Script.py => rscape analysis

Later research have used UCSC 470multiz way mammalian genomes
1.	Make bash file for bigbedtobed: make_bigbedtobed_sh.py
2.	Run bash file to run bigbedtobed: otherScripts/Rundirectory.sh
3.	Fix the maf file to the range: summer/run_fix_maf2.py
4.	Combine maf files together summer/final_maf.py
5.	Make bash file for maf2fasta: summer/Fill_ MAF_to_MFA.py
6.	Run bash for fasta: bash summer/Get_FASTA.sh
7.	Call linear alifold  otherScripts/Execute_Script.sh
8.	sbatch Script/call_fastatosto.sh => make fasta to sto and copy structures to sto file with bash
9.	Sbatch analyze/Rscape.sh => run rscape on stockhom files
10.	New_Script.py => rscape analysis => make a excel file
11.	Update_form.py to update names
12.	Add_percentage_for_plot.py to add percentage columns
13.	Get_plotting.py to get final plot



