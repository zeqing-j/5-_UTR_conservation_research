Human 5' UTR conservation research, alignment extracted from UCSC genome browser 470 multizway through Bigbedtobed
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
